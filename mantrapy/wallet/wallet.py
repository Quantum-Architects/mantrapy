import bech32
import ecdsa

from hdwallet import HDWallet, BIP32HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import ATOM as SYMBOL

from mantrapy.wallet.hashing import ripemd160


import json
import mnemonic


from binascii import (
    hexlify, unhexlify
)

from hashlib import sha256

from hdwallet.libs.bech32 import (
    bech32_encode, encode, bech32_decode, decode
)

from hdwallet.libs.ripemd160 import ripemd160
from hdwallet.libs.base58 import (
    check_encode, checksum_encode, check_decode, ensure_string
)


PATH = "m/44'/118'/0'/0/0"
TEST_MNEMONIC = "anger pencil awful note doctor like slide muffin hungry keen appear eight barrel stone quiz candy loud blush load three analyst buddy health member"

class Wallet:
    def __init__(self):
        self.mnemonic = ""
        self.wallet = None
        self.privkey =""
        # self.pubkey =""
        self.address=""
        self.sequence=""

def privkey_to_pubkey(privkey: str) -> bytes:
    key = ecdsa.SigningKey.from_string(unhexlify(privkey), curve= ecdsa.SECP256k1)
    # privkey_obj = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    pubkey_obj = key.get_verifying_key()
    return pubkey_obj.to_string("compressed")


def new_mnemonic():
    return mnemonic.Mnemonic(language="english").generate(strength=256)

def new_wallet_from_mnemonic(phrase:str):
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hd_wallet = hdwallet.from_mnemonic(phrase, "english")
    hd_wallet.from_path(PATH)
    return hd_wallet

def new_wallet():
    w = Wallet()
    w.mnemonic = new_mnemonic()
    w.mnemonic = TEST_MNEMONIC
    # w.mnemonic = "arch skill acquire abuse frown reject front second album pizza hill slogan guess random wonder benefit industry custom green ill moral daring glow elevator"


    print(w.mnemonic)
    temp= new_wallet_from_mnemonic(w.mnemonic)
    print(temp.p2wpkh_address())
    w.privkey = temp.private_key()
    compressed_public_key = privkey_to_pubkey(w.privkey)
    # w.pubkey = temp.public_key()

    # compressed_public_key = unhexlify(pubkey)
    public_key_hash = ripemd160(sha256(compressed_public_key).digest())
    # w.address= ensure_string(encode("cosmos", 0, public_key_hash))

    five_bit_r = bech32.convertbits(public_key_hash, 8, 5)
    w.address =  bech32.bech32_encode("mantra", five_bit_r)

    print(w.address)



def new_random_wallet():
    ENTROPY: str = generate_entropy()
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
    hdwallet.from_entropy(
        entropy=ENTROPY
    )
    hdwallet.from_path("")
    print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
    return hdwallet


