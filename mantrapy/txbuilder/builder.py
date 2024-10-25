class tx_builder:

    def __init__(self, addr: str)->None:
        self.addr = addr
        # TODO: use the get_account call to get the pubkey
        self.pubkey = None

    def bank_send(self, dst: str, amount:int, denom: str) -> str:

        return ""



