import requests

from mantrapy.types.account import Account, AccountResponse, PubKey
from mantrapy.types.bank import QueryAllBalancesResponse
from mantrapy.types.block import Block, BlockID, ResultBlock
from mantrapy.types.consensus import SyncInfo
from mantrapy.types.tx import ResultTx

"""
Querier defines a type to perform queries against the Mantra chain.
"""

TIMEOUT = 1
API = "https://api.mantrachain.io"
RPC = "https://rpc.mantrachain.io"

QUERY_PATHS = {
    "account": "/cosmos/auth/v1beta1/accounts/{address}",
    "balances": "/cosmos/bank/v1beta1/balances/{address}",
    "status": "/status",
    "block_by_hash": "block?hash={hash}",
    "block": "block?height={height}",
    "tx": "/tx?hash={_hash}",
}


class Querier:

    def __init__(self, api: str, rpc: str) -> None:
        self.api = api
        self.rpc = rpc

    def create_api_url(self, path: str) -> str:
        return self.api + path

    def create_rpc_url(self, path: str) -> str:
        return self.rpc + path

    # ACCOUNT
    def get_account(self, address: str) -> AccountResponse:
        url = self.create_api_url(QUERY_PATHS["account"].format(address=address))
        resp = requests.get(url, timeout=TIMEOUT)
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

    def get_balances(self, address: str) -> QueryAllBalancesResponse:
        url = self.create_api_url(QUERY_PATHS["balances"].format(address=address))
        resp = requests.get(url, timeout=TIMEOUT)

        print(resp)
        return QueryAllBalancesResponse.from_dict(data=resp.json())

    def get_height(self) -> str:
        url = self.create_rpc_url(QUERY_PATHS["status"])
        resp = requests.get(url, timeout=TIMEOUT)

        sync_info = SyncInfo.from_dict(resp.json()["result"]["sync_info"])
        return sync_info.latest_block_height

    def get_last_hash(self):
        url = self.create_rpc_url(QUERY_PATHS["status"])
        resp = requests.get(url, timeout=TIMEOUT)

        sync_info = SyncInfo.from_dict(resp.json()["result"]["sync_info"])
        return sync_info.latest_block_hash

    def get_block_by_height(self, height: str) -> ResultBlock:
        url = self.create_rpc_url(QUERY_PATHS["block"].format(height=height))
        resp = requests.get(url, timeout=TIMEOUT)

        result = resp.json()["result"]
        block = Block.from_dict(result["block"])
        block_id = BlockID.from_dict(result["block_id"])

        return ResultBlock(
            block_id=block_id,
            block=block,
        )

    def get_block_by_hash(self, _hash: str) -> ResultBlock:
        url = self.create_rpc_url(QUERY_PATHS["block_by_hash"].format(hash=_hash))
        resp = requests.get(url, timeout=TIMEOUT)

        result = resp.json()["result"]
        block = Block.from_dict(result["block"])
        block_id = BlockID.from_dict(result["block_id"])

        return ResultBlock(
            block_id=block_id,
            block=block,
        )

    def get_tx_by_hash(self, _hash: str):
        url = self.create_rpc_url(QUERY_PATHS["tx"].format(hash=_hash))
        resp = requests.get(url, timeout=TIMEOUT)

        return ResultTx.from_dict(resp.json()["result"])
