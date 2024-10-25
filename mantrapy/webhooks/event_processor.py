import requests


class EventProcessor:

    def __init__(self, webhook_url, process_event_fn):
        self.webhook_url = webhook_url
        self.process_fn = process_event_fn

    def process_events(self, events):
        processed_events = self.process_fn(events)
        print(len(processed_events))
        if len(processed_events) == 0:
            return
        notification = {'events': processed_events}
        print(notification)
        # self.send_notification(notification)

    def send_notification(self, notification):
        requests.post(self.webhook_url, json=notification)
