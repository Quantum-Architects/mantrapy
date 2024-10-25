from typing import List


class Attribute:
    key: str
    value: str


class CosmosEvent:
    type: str
    attributes: List[Attribute]


def _get_event(event_type, events: List[CosmosEvent]):
    for e in events:
        if e.type == event_type:
            return e


def _get_events_by_type(event_type, events: List[CosmosEvent]) -> List[CosmosEvent]:
    return [e for e in events if e["type"] == event_type]


def _get_events_by_attr_value(
    attribute: str, attr_val: str, events: List[CosmosEvent]
) -> List[CosmosEvent]:
    return [
        e
        for e in events
        if any(
            a.get("key") == attribute and a.get("value") == attr_val
            for a in e.get("attributes", [])
        )
    ]


def _get_events_by_value(attr_val, events: List[CosmosEvent]) -> List[CosmosEvent]:
    return [e for e in events if any(a["value"] == attr_val for a in e["attributes"])]


def _get_event_attribute(attribute, event: CosmosEvent):
    for a in event["attributes"]:
        if a.key == attribute:
            return a


def _get_module_events(module, events: List[CosmosEvent]):
    return _get_events_by_attr_value("module", module, events)


def _get_account_events(addr, events: List[CosmosEvent]):
    return _get_events_by_value(addr, events)


def _only_mod_events(events: List[CosmosEvent]) -> List[CosmosEvent]:
    if events is None:
        return []
    return [
        event
        for event in events
        if isinstance(event, dict)
        and isinstance(event.get("attributes"), dict)
        and "module" in event["attributes"]
    ]


def _get_account_modules_events(addr, events):
    all_events = _get_account_events(addr, events)
    return _only_mod_events(all_events)
