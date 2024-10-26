from mantrapy.client.client import Client
from mantrapy.constants.constants import Constants

constants = Constants()
client = Client(constants.api_endpoint, constants.rpc_endpoint)

height_resp = client.get_height()
print(height_resp.data)
