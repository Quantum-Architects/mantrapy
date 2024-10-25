from hashlib import sha256

import bech32

from mantrapy.wallet.hashing import ripemd160
from mantrapy.wallet.utils import new_hdwallet_from_mnemonic
from mantrapy.wallet.utils import new_mnemonic
from mantrapy.wallet.utils import privkey_to_pubkey

TEST_MNEMONIC = 'anger pencil awful note doctor like slide muffin hungry keen appear eight barrel stone quiz candy loud blush load three analyst buddy health member'
TEST_ADDRESS = 'mantra1qj5477l97xch25a7dfs6mjpcxp5n209purvvwg'


class Wallet:

    def __init__(self):
        self.mnemonic = ''
        self.privkey = ''
        self.address = ''


def random_wallet() -> Wallet:
    return wallet_from_mnemonic(new_mnemonic())


def test_wallet() -> Wallet:
    return wallet_from_mnemonic(TEST_MNEMONIC)


def wallet_from_mnemonic(mnemonic: str) -> Wallet:
    w = Wallet()
    w.mnemonic = mnemonic
    generator = new_hdwallet_from_mnemonic(w.mnemonic)
    w.privkey = generator.private_key()
    compressed_public_key = privkey_to_pubkey(w.privkey)
    public_key_hash = ripemd160(sha256(compressed_public_key).digest())
    five_bit_r = bech32.convertbits(public_key_hash, 8, 5)
    if five_bit_r is not None:
        w.address = bech32.bech32_encode('mantra', five_bit_r)
    else:
        print('invalid address')
        raise Exception('failed to generate address')

    return w
