import requests

from mantrapy.querier.types import QueryResponse
from mantrapy.types.cometbft.block import Block, BlockID, ResultBlock
from mantrapy.types.cometbft.consensus import SyncInfo
from mantrapy.types.cometbft.tx import ResultTx
from mantrapy.types.cosmossdk.account import Account, QueryAccountResponse
from mantrapy.types.cosmossdk.bank import QueryAllBalancesResponse

TIMEOUT = 10
MAX_RETRIES = 3
RETRY_DELAY = 1

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
    """
    Querier defines a type to perform queries against the Mantra chain.
    """

    def __init__(
        self,
        api: str,
        rpc: str,
        timeout: int = TIMEOUT,
        max_retries: int = MAX_RETRIES,
        retry_delay: int = RETRY_DELAY,
    ) -> None:
        """
        Initialize the class with base API and RPC URLs.
        """
        # Cosmos SDK endpoint.
        self.api = api.rstrip("/")
        # CometBFT endpoint.
        self.rpc = rpc.rstrip("/")

        # Requests parameters.
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def create_api_url(self, path: str) -> str:
        """
        Construct a full API URL by appending the given path to the base API URL.
        """
        return self.api + path

    def create_rpc_url(self, path: str) -> str:
        """
        Construct a full RPC URL by appending the given path to the base RPC URL.
        """
        return self.rpc + path

    def _make_request(self, url: str, method: str = "GET", **kwargs) -> QueryResponse:
        """
        Make HTTP request with retries and error handling.
        """

        # Repeat the request if it is failing
        for attempt in range(self.max_retries):
            try:
                response = requests.request(
                    method,
                    url,
                    timeout=self.timeout,
                    **kwargs,
                )
                data = response.json()

                return QueryResponse(
                    data=data,
                    status_code=response.status_code,
                )

            except Exception as e:
                print("CATCHING EXCEPTION")
                if attempt == self.max_retries - 1:
                    return QueryResponse(
                        error=str(e),
                        status_code=500,
                    )

        raise Exception("The request should be performed at least once.")

    def get_account(self, address: str) -> QueryResponse[QueryAccountResponse]:
        """
        Query the account associated with a particular address.
        """

        url = self.create_api_url(QUERY_PATHS["account"].format(address=address))
        resp = self._make_request(url)

        if not resp.is_success():
            return resp

        if not resp.data:
            raise Exception("Data returned by query is nil")

        try:

            account = Account.from_dict(resp.data)
            return QueryResponse(QueryAccountResponse(account=account))

        except KeyError as e:
            return QueryResponse(
                error=f"Invalid response format: {str(e)}",
                status_code=resp.status_code,
            )

    def get_balances(self, address: str) -> QueryResponse[QueryAllBalancesResponse]:
        """
        Query the balance associated with a particular address.
        """

        url = self.create_api_url(QUERY_PATHS["balances"].format(address=address))
        resp = self._make_request(url)

        if not resp.is_success():
            return resp

        if not resp.data:
            raise Exception("Data returned by query is nil")

        try:

            return QueryResponse(QueryAllBalancesResponse.from_dict(resp.data))

        except KeyError as e:
            return QueryResponse(
                error=f"Invalid response format: {str(e)}",
                status_code=resp.status_code,
            )

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
