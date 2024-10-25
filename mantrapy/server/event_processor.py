"""
Supported queries:
- module (e.g. module=staking)
- event type (e.g. event.type=transfer)
- event value (e.g. event.value=mantra1...)
- address (e.g. address=mantra1...)
- smart contract calls (e.g. contract=mantra1...)
"""

import re
from typing import Callable
from mantrapy.webhooks.event_processor import EventProcessor
from mantrapy.webhooks.hooks.address_activity import account_event_processor
from mantrapy.webhooks.modules.smart_contract import get_smart_contract_events
from mantrapy.webhooks.modules.utils import (
    get_events_by_type,
    get_events_by_value,
    get_module_events,
)


def get_event_processor(webhook_url: str, query: str) -> Callable:
    """Get an EventProcessor based on multiple query conditions."""

    # Split the query string by `&` to support multiple conditions
    conditions = query.split("&")
    condition_processors = []

    for condition in conditions:
        if "module=" in condition:
            module_value = extract_value(condition, "module")
            condition_processors.append(
                lambda events: get_module_events(module_value, events)
            )

        elif "type=" in condition:
            type_value = extract_value(condition, "type")
            condition_processors.append(
                lambda events: get_events_by_type(type_value, events)
            )

        elif "value=" in condition:
            value = extract_value(condition, "value")
            condition_processors.append(
                lambda events: get_events_by_value(value, events)
            )

        elif "address=" in condition:
            address_value = extract_value(condition, "address")
            condition_processors.append(account_event_processor(address_value))

        elif "contract=" in condition:
            contract_addr = extract_value(condition, "contract")
            condition_processors.append(
                lambda events, contract=contract_addr: get_smart_contract_events(
                    contract, events
                )
            )

        else:
            raise ValueError(f"Unsupported query condition: {condition}")

    # Combine all conditions for processing
    def combined_processor(events):
        filtered_events = events
        for processor in condition_processors:
            filtered_events = processor(filtered_events)
        return filtered_events

    return EventProcessor(webhook_url, combined_processor).process_events


def extract_value(query: str, key: str) -> str:
    """Extracts the value for a given key from the query string."""
    match = re.search(f"{key}=([^&]+)", query)
    if match:
        return match.group(1)
    raise ValueError(f"Invalid query format; missing {key}")
