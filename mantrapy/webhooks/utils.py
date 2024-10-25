import json


def format_event_json(event):
    return json.dumps(event, indent=4)
