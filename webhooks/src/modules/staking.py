from src.modules.utils import _get_events_by_attr_value, _get_module_events

MSG_DELEGATE = "/cosmos.staking.v1beta1.MsgDelegate"

def _get_staking_events(events):
    return _get_module_events("staking", events)


def _get_delegation_events(events):
    return _get_events_by_attr_value("action", MSG_DELEGATE, events)
