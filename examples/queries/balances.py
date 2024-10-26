from mantrapy.client.client import Client
from mantrapy.constants.constants import Constants

constants = Constants()
client = Client(constants.api_endpoint, constants.rpc_endpoint)

balances_resp = client.get_balances('mantra1n4u9s9h3c670s7wsfycf6v7d7f2t55ql9gm3sj')
print(balances_resp.data)
print(balances_resp.status_code)
