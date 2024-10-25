from google.protobuf.any_pb2 import Any
from google.protobuf.message import Message

from mantrapy.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from mantrapy.proto.cosmos.crypto.secp256k1.keys_pb2 import PubKey as Secp256PubKey
from mantrapy.proto.cosmos.tx.signing.v1beta1.signing_pb2 import SIGN_MODE_DIRECT
from mantrapy.proto.cosmos.tx.v1beta1.tx_pb2 import AuthInfo
from mantrapy.proto.cosmos.tx.v1beta1.tx_pb2 import Fee
from mantrapy.proto.cosmos.tx.v1beta1.tx_pb2 import ModeInfo
from mantrapy.proto.cosmos.tx.v1beta1.tx_pb2 import SignDoc
from mantrapy.proto.cosmos.tx.v1beta1.tx_pb2 import SignerInfo
from mantrapy.proto.cosmos.tx.v1beta1.tx_pb2 import TxBody


def create_body_bytes(msg: Message, memo: str):
    any = Any()
    any.Pack(msg, type_url_prefix='/')
    return TxBody(messages=[any], memo=memo)
    # body.messages.messages([any])
    # body.memo = memo
    # self.body = body


def create_fee(fee_amount: str, fee_denom: str, gas_limit: str):
    coin = Coin(denom=fee_denom, amount=fee_amount)
    return Fee(gas_limit=int(gas_limit), amount=[coin])


def create_signer_info(public_key_bytes: str, sequence: int):
    public_key = Any()
    public_key.Pack(Secp256PubKey(key=public_key_bytes), type_url_prefix='/')
    return SignerInfo(
        public_key=public_key,
        mode_info=ModeInfo(single=ModeInfo.Single(mode=SIGN_MODE_DIRECT)),
        sequence=sequence,
    )


def create_auth_info_bytes(signer_info: SignerInfo, fee: Fee):
    return AuthInfo(signer_infos=[signer_info], fee=fee)


def create_sig_doc(
    body: TxBody,
    auth_info: AuthInfo,
    chain_id: str,
    account_number: int,
):
    doc = SignDoc()
    doc.body_bytes = body.SerializeToString()
    doc.auth_info_bytes = auth_info.SerializeToString()
    doc.chain_id = chain_id
    doc.account_number = account_number
    return doc.SerializeToString()


# def create_signatures(self):
#     to_sign = self.create_sig_doc()
#     return self.builder.wallet.sign(sha3_256(to_sign).digest())


def create_tx_template(
    msg: Message,
    memo: str,
    fee_amount: str,
    fee_denom: str,
    gas_limit: str,
    pubkey: str,
    sequence: int,
):
    return create_body_bytes(msg, memo), create_auth_info_bytes(
        create_signer_info(pubkey, sequence),
        create_fee(fee_amount, fee_denom, gas_limit),
    )


#
#     def generate_tx(self,
#                     builder: TransactionBuilder,
#                     msg: Message,
#                     memo: str = MEMO,
#                     fee: str = FEE,
#                     gas_limit: str = GAS_LIMIT):
#         self.create_tx_template(builder, msg, memo, fee, gas_limit)
#         return self.create_tx_raw_with_class_info(self.create_signatures())
#
#
# def create_tx_raw(body_bytes, auth_info, signature):
#     tx = TxRaw()
#     tx.body_bytes = body_bytes
#     tx.auth_info_bytes = auth_info
#     tx.signatures.append(signature)
#     return tx
#
