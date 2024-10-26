from mantrapy.client.client import API
from mantrapy.client.client import Client
from mantrapy.client.client import RPC

client = Client(API, RPC)


tx_resp = client.get_tx_by_hash(
    '0xC414DBB9C80503DFF20684536710FD4FC0401B39C25B0171C752ABCE3907CD95',
)
print(tx_resp)
