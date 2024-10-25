from binascii import unhexlify
from typing import Any
import json
import ecdsa
import hashlib
import base64

def sign(tx:dict[str, Any], privkey_str:str) -> str:
    print(privkey_str)
    message_str = json.dumps(tx, separators=(",", ":"), sort_keys=True)
    print(message_str)
    message_bytes = message_str.encode("utf-8")

    privkey = ecdsa.SigningKey.from_string(unhexlify(privkey_str), curve=ecdsa.SECP256k1)
    signature_compact = privkey.sign_deterministic(
        message_bytes, hashfunc=hashlib.sha256, sigencode=ecdsa.util.sigencode_string_canonize
    )

    signature_base64_str = base64.b64encode(signature_compact).decode("utf-8")
    return signature_base64_str


def sign_document(doc: bytes, privkey_str:str) -> str:
    privkey = ecdsa.SigningKey.from_string(unhexlify(privkey_str), curve=ecdsa.SECP256k1)
    signature_compact = privkey.sign_deterministic(
        doc, hashfunc=hashlib.sha256, sigencode=ecdsa.util.sigencode_string_canonize
    )

    signature_base64_str = base64.b64encode(signature_compact).decode("utf-8")
    return signature_base64_str

