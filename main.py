# from mantrapy.txbuilder.builder import tx_builder
from mantrapy.wallet.wallet import wallet_from_mnemonic

# t = tx_builder("")
# t.bank_send("",1,"")

TEST_MNEMONIC = 'anger pencil awful note doctor like slide muffin hungry keen appear eight barrel stone quiz candy loud blush load three analyst buddy health member'  # noqa: E501
w = wallet_from_mnemonic(TEST_MNEMONIC)
print(w.address)
