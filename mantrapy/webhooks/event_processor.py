import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)


class EventProcessor:

    def __init__(self, webhook_url, process_event_fn):
        self.webhook_url = webhook_url
        self.process_fn = process_event_fn

    def process_events(self, events):
        processed_events = self.process_fn(events)
        print(len(processed_events))
        if len(processed_events) == 0:
            return
        notification = {"events": processed_events}
        print(notification)
        # self.send_notification(notification)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(requests.exceptions.RequestException),
    )
    def send_notification(self, notification):
        response = requests.post(self.webhook_url, json=notification)
        response.raise_for_status()
