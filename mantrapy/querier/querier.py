import requests

from mantrapy.types.account import Account, AccountResponse, PubKey

"""
"""

ENDPOINT = "https://api.mantrachain.io"


class Querier:

    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint

    def create_query_url(self, path: str) -> str:
        return self.endpoint + path

    # def get_params(self) -> :
    #     path = "/cosmos/auth/v1beta1/params"
    #     resp = requests.get(self.create_query_url(path))
    #     json_resp = resp.json()
    #     return

    def get_account(self, address: str) -> AccountResponse:
        path = f"/cosmos/auth/v1beta1/accounts/{address}"
        resp = requests.get(self.create_query_url(path))
        json_resp = resp.json()

        account_data = json_resp["account"]
        pub_key_data = account_data["pub_key"]
        pub_key = PubKey(key_type=pub_key_data["@type"], key=pub_key_data["key"])

        account = Account(
            key_type=account_data["@type"],
            address=account_data["address"],
            pub_key=pub_key,
            account_number=account_data["account_number"],
            sequence=account_data["sequence"],
        )

        return AccountResponse(account=account)

    def get_balances(self):
        return

    def get_height(self)
