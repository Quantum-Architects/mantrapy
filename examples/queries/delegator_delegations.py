from mantrapy.client.client import API, RPC, Client

client = Client(API, RPC)

# https://api.mantrachain.io/cosmos/staking/v1beta1/delegations/mantra10zd2np34ltzt9wr54u4xkqzy8u4lr2yqk3f7tz
tx_resp = client.get_delegator_delegations(
    "mantra10zd2np34ltzt9wr54u4xkqzy8u4lr2yqk3f7tz"
)
print(tx_resp.data)
