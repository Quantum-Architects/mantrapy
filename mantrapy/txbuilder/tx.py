from typing import Any

def create_tx(chain_id: str, account_number: str, gas:str, fee_amount:str, fee_denom:str, memo:str, sequence:str, msgs: list[Any]) -> dict[str, Any]:
    return {
        "chain_id": chain_id,
        "account_number": account_number,
        "fee": {
            "gas": gas,
            "amount": [{"amount": fee_amount, "denom": fee_denom}],
        },
        "memo": memo,
        "sequence": sequence,
        "msgs": msgs,
    }

def create_tx2(chain_id: str, account_number: str, gas:str, fee_amount:str, fee_denom:str, memo:str, sequence:str, msgs: list[Any],pubkey:str, sign:str) -> dict[str, Any]:
    return {
        "chain_id": chain_id,
        "account_number": account_number,
        "fee": {
            "gas": gas,
            "amount": [{"amount": fee_amount, "denom": fee_denom}],
        },
        "signatures": [
        {
            "signature": sign,
            "pub_key": {"type": "tendermint/PubKeySecp256k1", "value": pubkey},
        }],
        "memo": memo,
        "sequence": sequence,
        "msgs": msgs,
    }
