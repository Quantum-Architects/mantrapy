from src.modules.smart_contract import _get_smart_contracts_events
from src.webhooks.webhook import Webhook


class SmartContractWebhook(Webhook):
    def __init__(self, websocket_url, webhook_url):
        # Customize process function with the specific address
        process_fn = lambda events: _get_smart_contracts_events(events)
        # Initialize the base Webhook with the custom process function
        super().__init__(websocket_url, webhook_url, process_fn)
