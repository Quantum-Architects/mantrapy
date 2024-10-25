"""
Supported queries:
- module (e.g. module=staking)
- event type (e.g. event.type=transfer)
- event value (e.g. event.value=mantra1...)
- addess (e.g. address=mantra1...)
- smart contract calls (e.g. contract=mantra1...)
"""

from webhooks.event_processor import EventProcessor
from webhooks.hooks.address_activity import account_event_processor
from webhooks.modules.smart_contract import get_smart_contract_events
from webhooks.modules.utils import (
    get_events_by_type,
    get_events_by_value,
    get_module_events,
)


def get_event_processor(webhook_url: str, query: str) -> EventProcessor:
    """Get the appropriate EventProcessor based on the query type."""
    if "module=" in query:
        module_value = extract_value(query, "module")
        return EventProcessor(
            webhook_url, lambda events: get_module_events(module_value, events)
        )

    elif "event.type=" in query:
        event_type_value = extract_value(query, "event.type")
        return EventProcessor(
            webhook_url,
            lambda events: get_events_by_type(event_type_value, events),
        )

    elif "event.value=" in query:
        event_value = extract_value(query, "event.value")
        return EventProcessor(
            webhook_url, lambda events: get_events_by_value(event_value, events)
        )

    elif "address=" in query:
        address_value = extract_value(query, "address")
        return EventProcessor(webhook_url, account_event_processor(address_value))

    elif "contract=" in query:
        contract_addr = extract_value(query, "contract")
        return EventProcessor(
            webhook_url,
            lambda events: get_smart_contract_events(contract_addr, events),
        )

    else:
        raise ValueError(f"Unsupported query: {query}")


def extract_value(query: str, key: str) -> str:
    """Extract the value for the specified key from the query string."""
    key_value_pair = f"{key}="
    if key_value_pair in query:
        start_index = query.index(key_value_pair) + len(key_value_pair)
        end_index = query.find("&", start_index)
        if end_index == -1:  # If no '&' is found, get till the end of the string
            end_index = len(query)
        return query[start_index:end_index]
    return None
