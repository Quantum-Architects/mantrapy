import asyncio

from src.config import Config
from src.webhooks.address_activity import AddressActivityWebhook
from src.webhooks.smart_contract import SmartContractWebhook

address = 'mantra13pxn9n3qw79e03844rdadagmg0nshmwf4txc8r'


async def main():
    config = Config()
    webhook = SmartContractWebhook(
        websocket_url=config.websocket_url,
        webhook_url=config.webhook_url,
    )
    await webhook.listen()


# Run the main async function
asyncio.run(main())
