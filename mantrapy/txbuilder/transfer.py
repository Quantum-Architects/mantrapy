def generate_msg_send(sender, to, amount, denom):
    return {
        "type": "cosmos-sdk/MsgSend",
        "value": {
            "from_address": sender,
            "to_address": to,
            "amount": [{"denom": denom, "amount": str(amount)}],
        },
    }
