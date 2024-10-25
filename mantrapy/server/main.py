from contextlib import asynccontextmanager
import json
from uuid import uuid4
from fastapi import FastAPI, HTTPException, WebSocket, BackgroundTasks
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import asyncio

from event_processor import get_event_processor
from webhooks.chain_client import ChainClient
from databases import SessionLocal, Webhook


app = FastAPI()
websocket_url = "ws://example.com/socket"  # Replace with your WebSocket URL
chain_client = ChainClient(websocket_url)

# In-memory cache for registered webhooks
registered_hooks_cache = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to node via WS
    await chain_client.connect()  # Make sure to await the connection if it is async

    with SessionLocal() as db:
        existing_hooks = db.query(Webhook).all()
        for hook in existing_hooks:
            try:
                # Attempt to create an event processor
                processor = get_event_processor(hook.url, hook.query)
                # Cache the hooks and their corresponding event processor
                registered_hooks_cache[hook.id] = processor
            except ValueError as e:
                # Handle the case where the query is unsupported
                print(f"Error creating EventProcessor for hook ID {hook.id}: {e}")
                # Optionally, log the error or raise an HTTP exception
                # You might want to log the error or handle it according to your app's needs
                # For example, you could raise an HTTPException:
                # raise HTTPException(status_code=400, detail=str(e))

    # Start the event processor in the background
    asyncio.create_task(process_events())
    yield
    # Close the WebSocket connection on server shutdown
    if chain_client.websocket:
        await chain_client.websocket.close()


async def process_events():
    """Listen for events from the ChainClient and post to registered webhooks."""
    async for ws_event in chain_client.subscribe("tm.event='Tx'"):
        # Decode the incoming message if it's JSON
        try:
            if isinstance(ws_event, str):
                ws_event = json.loads(ws_event)
            if "events" in ws_event.get(
                "result", {}
            ) and "message.msg_index" in ws_event["result"].get("events", {}):
                events = ws_event["result"]["data"]["value"]["TxResult"]["result"][
                    "events"
                ]
                # Iterate through the cached hooks and post the event data
            for _, event_processor in registered_hooks_cache.items():
                await event_processor(events)
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing event data: {e}")
            print("Raw event data:", ws_event)


@app.post("/webhooks/")
async def create_webhook(url: str, query: str):
    """Create a new webhook and persist it in the database."""
    # Attempt to create an event processor
    try:
        processor = get_event_processor(url, query)
    except ValueError as e:
        # Return a 404 error if get_event_processor fails
        raise HTTPException(status_code=404, detail=str(e))

    # Generate a new unique hook ID (UUID)
    hook_id = str(uuid4())

    with SessionLocal() as db:
        new_webhook = Webhook(id=hook_id, query=query, url=url)
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
