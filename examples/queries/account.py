from mantrapy.client.client import API
from mantrapy.client.client import Client
from mantrapy.client.client import RPC

client = Client(API, RPC)

account_resp = client.get_account('mantra1n4u9s9h3c670s7wsfycf6v7d7f2t55ql9gm3sj')
print(account_resp.data)
print(account_resp.status_code)
