from mantrapy.client.client import Client
from mantrapy.constants.constants import Constants

constants = Constants()
client = Client(constants.api_endpoint, constants.rpc_endpoint)

# https://www.mintscan.io/mantra/block/392617?sector=events
height_resp = client.get_block_by_height(392617)
print(height_resp.data)

height_resp = client.get_block_by_hash(
    "0x744B0E582780B790B739E81FF79E5F19E4200CF86E8302969CC1C898C798EC4B"
)
print(height_resp.data)
