import asyncio

from mantrapy.webhooks.config import Config
from mantrapy.webhooks.hooks.smart_contract import SmartContractWebhook


async def main():
    config = Config()
    webhook = SmartContractWebhook(
        websocket_url=config.websocket_url,
        webhook_url=config.webhook_url,
    )
    await webhook.listen()


# Run the main async function
asyncio.run(main())
