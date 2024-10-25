from mantrapy.constants.constants import Constants
from mantrapy.txbuilder.transaction import create_fee


class tx_builder:

    def __init__(self, addr: str, is_testnet: bool = False) -> None:
        self.addr = addr
        # TODO: use the get_account call to get the pubkey
        self.pubkey = None
        self.constants = Constants()
        if is_testnet:
            self.constants.testnet()

    def bank_send(self, dst: str, amount: int, denom: str) -> str:
        create_fee('1', 'a', '1')
        return 'a'
