from mantrapy.txbuilder.builder import TxBuilder
from mantrapy.wallet.wallet import wallet_from_mnemonic

TEST_MNEMONIC = 'anger pencil awful note doctor like slide muffin hungry keen appear eight barrel stone quiz candy loud blush load three analyst buddy health member'  # noqa: E501
w = wallet_from_mnemonic(TEST_MNEMONIC)

builder = TxBuilder(w, is_testnet=True)
body,auth,sign_doc = builder.bank_send("mantra1wf2eqtltm35tc5dllhp9uuzy66qvuwhve7zzgr", 1, "uom")
resp = builder.broadcast_tx(body, auth, builder.sign_message(sign_doc))
print(resp)
