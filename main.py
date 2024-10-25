# from mantrapy.txbuilder.builder import tx_builder
from mantrapy.wallet.wallet import test_wallet

# t = tx_builder("")
# t.bank_send("",1,"")
w = test_wallet()
print(w.address)
