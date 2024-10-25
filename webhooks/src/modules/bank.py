from src.modules.utils import _get_events_by_attr_value
from src.modules.utils import _get_module_events

MSG_BANK_SEND = '/cosmos.bank.v1beta1.MsgSend'


def _get_bank_events(events):
    return _get_module_events('bank', events)


def _get_bank_events_for_addr(addr, events):
    return _get_module_events('bank', events)


def _get_bank_tranfer_events(events):
    return _get_events_by_attr_value('action', MSG_BANK_SEND, events)
