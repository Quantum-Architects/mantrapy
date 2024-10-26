from mantrapy.client.client import API
from mantrapy.client.client import Client
from mantrapy.client.client import RPC

client = Client(API, RPC)

balances_resp = client.get_balances('mantra1n4u9s9h3c670s7wsfycf6v7d7f2t55ql9gm3sj')
print(balances_resp.data)
print(balances_resp.status_code)
