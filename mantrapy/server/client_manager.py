import asyncio
from server.databases import Webhook, SessionLocal
from webhooks.chain_client import ChainClient


class ChainClientManager:
    _instance = None

    def __new__(cls, websocket_url):
        if cls._instance is None:
            cls._instance = super(ChainClientManager, cls).__new__(cls)
            cls._instance.websocket_url = websocket_url
            cls._instance.client = ChainClient(websocket_url)
            cls._instance.hooks = set()  # To track active hooks
        return cls._instance

    async def ensure_connection(self):
        """Ensure that the WebSocket connection is established if there are hooks."""
        if len(self.hooks) > 0:
            await self.client.connect()

    def register_hook(self, hook_id):
        """Register a new webhook and establish a connection if necessary."""
        self.hooks.add(hook_id)
        asyncio.create_task(self.ensure_connection())

    def unregister_hook(self, hook_id):
        """Unregister a webhook and close connection if there are no active hooks."""
        self.hooks.discard(hook_id)
        if len(self.hooks) == 0:
            asyncio.create_task(self.close_connection())

    async def close_connection(self):
        """Close the WebSocket connection if there are no active hooks."""
        if self.client.websocket and self.client.websocket.open:
            await self.client.websocket.close()
            self.client.websocket = None
            print("WebSocket connection closed.")

    async def subscribe(self, query):
        """Subscribe to a query and yield messages."""
        return self.client.subscribe(query)

    async def load_hooks(self):
        """Load hooks from the database."""
        with SessionLocal() as db:
            existing_hooks = db.query(Webhook).all()
            for hook in existing_hooks:
                self.register_hook(hook.hook_id)
