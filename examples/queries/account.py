from mantrapy.client.client import Client
from mantrapy.constants.constants import Constants

constants = Constants()
client = Client(constants.api_endpoint, constants.rpc_endpoint)

account_resp = client.get_account("mantra1n4u9s9h3c670s7wsfycf6v7d7f2t55ql9gm3sj")
print(account_resp.data)
print(account_resp.status_code)
