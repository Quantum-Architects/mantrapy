import json
from typing import Any

def tx_to_txbytes(msgs: list[Any], gas:str, fee_denom:str, fee_amount:str, memo:str, signature: str, pubkey:str, account_number:str, sequence:str) -> str:
    temp = {
        "tx": {
            "msg": msgs,
            "fee": {
                "gas": gas,
                "amount": [{"denom": fee_denom, "amount": fee_amount}],
            },
            "memo": memo,
            "signatures": [
                {
                    "signature": signature,
                    "pub_key": {"type": "tendermint/PubKeySecp256k1", "value": pubkey},
                    "account_number": account_number,
                    "sequence": sequence,
                }
            ],
        },
        "mode": "sync",
    }

    # temp = {
    #     "tx": {
    #         "msg": msgs,
    #         "fee": {
    #             "gas": gas,
    #             "amount": [{"denom": fee_denom, "amount": fee_amount}],
    #         },
    #         "signatures": [
    #             {
    #                 "signature": signature,
    #                 "pub_key": {"type": "tendermint/PubKeySecp256k1", "value": pubkey},
    #             }
    #         ],
    #     },
    #     "memo": "",
    #     "chain_id": "mantra-dukong-1",
    #     "account_number": account_number,
    #     "sequence": sequence,
    # }


    return json.dumps(temp, separators=(",", ":"), sort_keys=True)

