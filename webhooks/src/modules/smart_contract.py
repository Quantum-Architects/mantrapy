from src.modules.utils import (
    _get_events_by_type,
    _get_events_by_value,
)


def _get_smart_contracts_events(events):
    # CosmWasm contracts calls are recorded in a 'wasm' event type
    return _get_events_by_type("wasm", events)


def _get_smart_contract_events(contract_addr, events):
    # CosmWasm contracts calls are recorded in a 'wasm' event type
    sc_events = _get_smart_contracts_events(events)
    return _get_events_by_value(contract_addr, sc_events)
