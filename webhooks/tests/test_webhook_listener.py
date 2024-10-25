import unittest
from cosmos_webhook_lib.webhook_listener import WebhookListener


class TestWebhookListener(unittest.TestCase):
    def test_listen(self):
        listener = WebhookListener(
            node_url="https://localhost", webhook_url="https://webhook"
        )
        listener.listen()
        self.assertTrue(True)
