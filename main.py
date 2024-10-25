import requests
import base64
import json
from mantrapy.wallet.wallet import wallet_from_mnemonic
from mantrapy.querier.querier import Querier,API,RPC
from mantrapy.txbuilder.transfer import  generate_msg_send
from mantrapy.txbuilder.tx import  create_tx,create_tx2
from mantrapy.txbuilder.broadcast import  tx_to_txbytes
from mantrapy.txbuilder.signer import  sign, sign_document
from mantrapy.txbuilder.transaction import create_tx_template, create_sig_doc, create_tx_raw

from mantrapy.proto.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from google.protobuf.json_format import Parse


# t = tx_builder("")
# t.bank_send("",1,"")

TEST_MNEMONIC = 'anger pencil awful note doctor like slide muffin hungry keen appear eight barrel stone quiz candy loud blush load three analyst buddy health member'  # noqa: E501
w = wallet_from_mnemonic(TEST_MNEMONIC)
print(w.address)

q = Querier(API, RPC)
acc = q.get_account(w.address)

print(q.get_account(w.address).account.pub_key.key)

raw_msg = {
    'fromAddress': "mantra1qj5477l97xch25a7dfs6mjpcxp5n209purvvwg",
    'toAddress': "mantra1wf2eqtltm35tc5dllhp9uuzy66qvuwhve7zzgr",
    'amount': [{
        'denom': "uom",
        'amount': str(1),
    }],
}
msg= Parse(json.dumps(raw_msg), MsgSend())
print (msg)
pubkey =  base64.b64decode(acc.account.pub_key.key)
a, b = create_tx_template(msg,"", "1000","uom", "70000",pubkey, int(acc.account.sequence))
print(a)
print(b)
c = create_sig_doc(a,b,"mantra-dukong-1",int(acc.account.account_number))
print(c)

signed = sign_document(c,w.privkey)
print(signed)

signed_bytes = base64.b64decode(signed)

txraw= create_tx_raw(a.SerializeToString(), b.SerializeToString(), signed_bytes)
print(txraw)
txbytes = txraw.SerializeToString()
tx_bytes_in_base64 = base64.b64encode(txbytes).decode()
b = {
    "tx_bytes": tx_bytes_in_base64,
    "mode": "BROADCAST_MODE_BLOCK"
  }
print(b)

resp = requests.post(url=API+"/cosmos/tx/v1beta1/txs",data=b)
print(resp)
print(resp.status_code)
print(resp.json())



# msg_send = generate_msg_send(
#         sender="mantra1qj5477l97xch25a7dfs6mjpcxp5n209purvvwg",
#         to="mantra1wf2eqtltm35tc5dllhp9uuzy66qvuwhve7zzgr",
#         amount="1",
#         denom="uom",
#         )
# tx = create_tx(
#         chain_id="mantra-dukong-1",
#         account_number= acc.account.account_number,
#         gas="70000",
#         fee_amount="1000",
#         fee_denom="uom",
#         memo="",
#         sequence= acc.account.sequence,
#         msgs=[msg_send],
#         )
#
# signed = sign(tx, w.privkey)
# bytesToBroadcast = create_tx2(
#         chain_id="mantra-dukong-1",
#         account_number= acc.account.account_number,
#         gas="70000",
#         fee_amount="1000",
#         fee_denom="uom",
#         memo="",
#         sequence= acc.account.sequence,
#         msgs=[msg_send],
#         pubkey=acc.account.pub_key.key,
#         sign=signed,
#         )
#
# # bytesToBroadcast = tx_to_txbytes(
# #         msgs=[msg_send],
# #         gas="70000",
# #         fee_denom="uom",
# #         fee_amount="1000",
# #         memo="",
# #         signature=signed,
# #         pubkey=acc.account.pub_key.key,
# #         account_number=acc.account.account_number,
# #         sequence=acc.account.sequence,
# #         )
#
# print(bytesToBroadcast)
# a = json.dumps(bytesToBroadcast, separators=(",", ":"), sort_keys=True)
# print(a)
#
# encoded_tx = base64.b64encode(a.encode()).decode()
# print(encoded_tx)
#
# # curl -X POST http://localhost:1317/cosmos/tx/v1beta1/txs \
# #   -d '{
# #     "tx_bytes": "Base64_encoded_signed_tx",
# #     "mode": "BROADCAST_MODE_BLOCK"
# #   }' \
# #   -H "Content-Type: application/json"
#
# b = {
#     "tx_bytes": encoded_tx,
#     "mode": "BROADCAST_MODE_BLOCK"
#   }
# print(b)
#
# b = 'eyJhY2NvdW50X251bWJlciI6IjIzMDk0MiIsImNoYWluX2lkIjoibWFudHJhLWR1a29uZy0xIiwiZmVlIjp7ImFtb3VudCI6W3siYW1vdW50IjoiMTAwMCIsImRlbm9tIjoidW9tIn1dLCJnYXMiOiI3MDAwMCJ9LCJtZW1vIjoiIiwibXNncyI6W3sidHlwZSI6ImNvc21vcy1zZGsvTXNnU2VuZCIsInZhbHVlIjp7ImFtb3VudCI6W3siYW1vdW50IjoiMSIsImRlbm9tIjoidW9tIn1dLCJmcm9tX2FkZHJlc3MiOiJtYW50cmExcWo1NDc3bDk3eGNoMjVhN2RmczZtanBjeHA1bjIwOXB1cnZ2d2ciLCJ0b19hZGRyZXNzIjoibWFudHJhMXdmMmVxdGx0bTM1dGM1ZGxsaHA5dXV6eTY2cXZ1d2h2ZTd6emdyIn19XSwic2VxdWVuY2UiOiIxIiwic2lnbmF0dXJlcyI6W3sicHViX2tleSI6eyJ0eXBlIjoidGVuZGVybWludC9QdWJLZXlTZWNwMjU2azEiLCJ2YWx1ZSI6IkFoVHlYRjcwb3VyWlArakVwU2Z6WTVzOUJGK3NjMCs1T3kyZ2F3TDFza0tJIn0sInNpZ25hdHVyZSI6IklpK1dkRFh4NG1LaFBaMHUvZlpkclhTd0FDTFE3cVIyL2xsRzJhcDlHUjBLZWlkdFMyZDBmV2k0VHZCdVBRQUMrQW9URTNRWTJLbUY2a2VaenFJeXVRPT0ifV19Cg=='
#
# resp = requests.post(url=API+"/cosmos/tx/v1beta1/txs",data=b)
# print(resp)
# print(resp.status_code)
# print(resp.json())
