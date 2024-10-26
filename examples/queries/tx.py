from mantrapy.client.client import Client
from mantrapy.constants.constants import Constants

constants = Constants()
client = Client(constants.api_endpoint, constants.rpc_endpoint)


tx_resp = client.get_tx_by_hash(
    '0xC414DBB9C80503DFF20684536710FD4FC0401B39C25B0171C752ABCE3907CD95',
)
print(tx_resp)
