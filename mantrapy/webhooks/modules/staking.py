from mantrapy.webhooks.modules.utils import get_events_by_attr_value
from mantrapy.webhooks.modules.utils import _get_module_events

MSG_DELEGATE = '/cosmos.staking.v1beta1.MsgDelegate'


def get_staking_events(events):
    return _get_module_events('staking', events)


def get_delegation_events(events):
    return get_events_by_attr_value('action', MSG_DELEGATE, events)
