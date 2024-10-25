from src.modules.tokenfactory import _get_token_factory_events
from src.webhooks.webhook import Webhook


class TokenFactoryWebhook(Webhook):
    def __init__(self, websocket_url, webhook_url):
        # Customize process function with the specific address
        process_fn = lambda events: _get_token_factory_events(events)
        # Initialize the base Webhook with the custom process function
        super().__init__(websocket_url, webhook_url, process_fn)
