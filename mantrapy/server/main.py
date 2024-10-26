from contextlib import asynccontextmanager
import json
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import asyncio

from pydantic import BaseModel

from mantrapy.server.event_processor import get_event_processor
from mantrapy.webhooks.chain_client import ChainClient
from mantrapy.server.databases import SessionLocal, Webhook


# data model for the request body
class WebhookRequest(BaseModel):
    url: str
    query: str


websocket_url = (
    "wss://rpc.hongbai.mantrachain.io:443/websocket"  # Replace with your WebSocket URL
)
chain_client = ChainClient(websocket_url)

# In-memory cache for registered webhooks
registered_hooks_cache = {}


async def run_process_fn(process_fn, events, hook_id):
    """Wrapper to run process_fn with error handling."""
    try:
        await process_fn(events)
    except Exception as e:
        print(f"Error processing event in hook {hook_id}: {e}")


async def process_events():
    """Listen for events from the ChainClient and post to registered webhooks."""
    async for ws_event in chain_client.subscribe("tm.event='Tx'"):
        try:
            # Decode the incoming message if it's JSON
            if isinstance(ws_event, str):
                ws_event = json.loads(ws_event)
            if "events" in ws_event.get(
                "result", {}
            ) and "message.msg_index" in ws_event["result"].get("events", {}):
                events = ws_event["result"]["data"]["value"]["TxResult"]["result"][
                    "events"
                ]

                # Create a list to hold all processing tasks
                tasks = []

                # Iterate through the cached hooks and create a task for each process_fn
                for hook_id, process_fn in registered_hooks_cache.items():
                    tasks.append(
                        asyncio.create_task(run_process_fn(process_fn, events, hook_id))
                    )

                # Wait for all tasks to complete
                await asyncio.gather(*tasks)

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing event data: {e}")
            print("Raw event data:", ws_event)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    await chain_client.connect()  # Connect to WebSocket
    with SessionLocal() as db:
        existing_hooks = db.query(Webhook).all()
        for hook in existing_hooks:
            try:
                # Attempt to create an event processor
                processor = get_event_processor(hook.id, hook.url, hook.query)
                # Cache the hooks and their corresponding event processor
                registered_hooks_cache[hook.id] = processor
            except ValueError as e:
                print(f"Error creating EventProcessor for hook ID {hook.id}: {e}")

    # Start the event processor in the background
    asyncio.create_task(process_events())
    yield
    # Close the WebSocket connection on server shutdow
    if chain_client.websocket:
        try:
            await chain_client.websocket.close()
        except Exception as e:
            print(f"Error closing ws connection: {e}")


app = FastAPI(lifespan=lifespan)


@app.post("/webhooks/")
async def create_webhook(req: WebhookRequest):
    """Create a new webhook and persist it in the database."""
    # Generate a new unique hook ID (UUID)
    hook_id = str(uuid4())
    # Attempt to create an event processor
    try:
        processor = get_event_processor(hook_id, req.url, req.query)
    except ValueError as e:
        # Return a 404 error if get_event_processor fails
        raise HTTPException(status_code=404, detail=str(e))

    with SessionLocal() as db:
        new_webhook = Webhook(id=hook_id, query=req.query, url=req.url)
        db.add(new_webhook)
        db.commit()

    # Cache the new hook
    registered_hooks_cache[hook_id] = processor
    return {"message": "Webhook created", "hook_id": hook_id}


@app.delete("/webhooks/{hook_id}")
async def delete_webhook(hook_id: str):
    """Remove a webhook from the database."""
    with SessionLocal() as db:
        webhook = db.query(Webhook).filter(Webhook.id == hook_id).first()
        if not webhook:
            raise HTTPException(status_code=404, detail="Webhook not found")

        db.delete(webhook)
        db.commit()

    # Remove from cache
    registered_hooks_cache.pop(hook_id, None)
    return {"message": "Webhook deleted", "hook_id": hook_id}


@app.get("/webhooks/")
async def get_webhooks():
    """List webhooks."""
    with SessionLocal() as db:
        webhooks = db.query(Webhook).all()

    return {"hooks": webhooks}


@app.get("/webhooks/{hook_id}")
async def get_webhook(hook_id: str):
    """Get webhook by ID."""
    with SessionLocal() as db:
        webhook = db.query(Webhook).filter(Webhook.id == hook_id).first()
        if not webhook:
            raise HTTPException(status_code=404, detail="Webhook not found")

    return {"hook": webhook}
