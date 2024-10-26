from mantrapy.client.client import API, RPC, Client

client = Client(API, RPC)


height_resp = client.get_height()
print(height_resp.data)
