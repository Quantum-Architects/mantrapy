from mantrapy.client.client import API
from mantrapy.client.client import Client
from mantrapy.client.client import RPC

client = Client(API, RPC)


height_resp = client.get_height()
print(height_resp.data)
