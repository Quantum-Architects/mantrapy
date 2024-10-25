class PubKey:

    def __init__(self, key_type: str, key: str):
        self.key_type = key_type
        self.key = key


class Account:

    def __init__(
        self,
        key_type: str,
        address: str,
        pub_key: PubKey,
        account_number: str,
        sequence: str,
    ):
        self.key_type = key_type
        self.address = address
        self.pub_key = pub_key
        self.account_number = account_number
        self.sequence = sequence


class AccountResponse:

    def __init__(self, account: Account):
        self.account = account
