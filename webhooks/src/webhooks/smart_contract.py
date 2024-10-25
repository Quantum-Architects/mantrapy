from src.modules.smart_contract import _get_smart_contracts_events
from src.webhooks.webhook import Webhook


class SmartContractWebhook(Webhook):

    def __init__(self, websocket_url, webhook_url):
        # Initialize the base Webhook with the custom process function
        super().__init__(
            websocket_url,
            webhook_url,
            _get_smart_contracts_events,
        )
