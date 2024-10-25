# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmwasm/wasm/v1/proposal.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\"\xbd\x01\n\x11StoreCodeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06run_as\x18\x03 \x01(\t\x12(\n\x0ewasm_byte_code\x18\x04 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCode\x12>\n\x16instantiate_permission\x18\x07 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\"\x8d\x02\n\x1bInstantiateContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06run_as\x18\x03 \x01(\t\x12\r\n\x05\x61\x64min\x18\x04 \x01(\t\x12\x1b\n\x07\x63ode_id\x18\x05 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\r\n\x05label\x18\x06 \x01(\t\x12#\n\x03msg\x18\x07 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12Z\n\x05\x66unds\x18\x08 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\x91\x01\n\x17MigrateContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x63ontract\x18\x04 \x01(\t\x12\x1b\n\x07\x63ode_id\x18\x05 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12#\n\x03msg\x18\x06 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\"q\n\x14SudoContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x63ontract\x18\x03 \x01(\t\x12#\n\x03msg\x18\x04 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\"\xe0\x01\n\x17\x45xecuteContractProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06run_as\x18\x03 \x01(\t\x12\x10\n\x08\x63ontract\x18\x04 \x01(\t\x12#\n\x03msg\x18\x05 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12Z\n\x05\x66unds\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"t\n\x13UpdateAdminProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\'\n\tnew_admin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"new_admin\"\x12\x10\n\x08\x63ontract\x18\x04 \x01(\t\"J\n\x12\x43learAdminProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x63ontract\x18\x03 \x01(\t\"\x92\x01\n\x10PinCodesProposal\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12\x30\n\x08\x63ode_ids\x18\x03 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\"\"\x94\x01\n\x12UnpinCodesProposal\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12\x30\n\x08\x63ode_ids\x18\x03 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\"\"w\n\x12\x41\x63\x63\x65ssConfigUpdate\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x44\n\x16instantiate_permission\x18\x02 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigB\x04\xc8\xde\x1f\x00\"\xba\x01\n\x1fUpdateInstantiateConfigProposal\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12I\n\x15\x61\x63\x63\x65ss_config_updates\x18\x03 \x03(\x0b\x32$.cosmwasm.wasm.v1.AccessConfigUpdateB\x04\xc8\xde\x1f\x00\x42\x34Z&github.com/CosmWasm/wasmd/x/wasm/types\xd8\xe1\x1e\x00\xc8\xe1\x1e\x00\xa8\xe2\x1e\x01\x62\x06proto3')



_STORECODEPROPOSAL = DESCRIPTOR.message_types_by_name['StoreCodeProposal']
_INSTANTIATECONTRACTPROPOSAL = DESCRIPTOR.message_types_by_name['InstantiateContractProposal']
_MIGRATECONTRACTPROPOSAL = DESCRIPTOR.message_types_by_name['MigrateContractProposal']
_SUDOCONTRACTPROPOSAL = DESCRIPTOR.message_types_by_name['SudoContractProposal']
_EXECUTECONTRACTPROPOSAL = DESCRIPTOR.message_types_by_name['ExecuteContractProposal']
_UPDATEADMINPROPOSAL = DESCRIPTOR.message_types_by_name['UpdateAdminProposal']
_CLEARADMINPROPOSAL = DESCRIPTOR.message_types_by_name['ClearAdminProposal']
_PINCODESPROPOSAL = DESCRIPTOR.message_types_by_name['PinCodesProposal']
_UNPINCODESPROPOSAL = DESCRIPTOR.message_types_by_name['UnpinCodesProposal']
_ACCESSCONFIGUPDATE = DESCRIPTOR.message_types_by_name['AccessConfigUpdate']
_UPDATEINSTANTIATECONFIGPROPOSAL = DESCRIPTOR.message_types_by_name['UpdateInstantiateConfigProposal']
StoreCodeProposal = _reflection.GeneratedProtocolMessageType('StoreCodeProposal', (_message.Message,), {
  'DESCRIPTOR' : _STORECODEPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.StoreCodeProposal)
  })
_sym_db.RegisterMessage(StoreCodeProposal)

InstantiateContractProposal = _reflection.GeneratedProtocolMessageType('InstantiateContractProposal', (_message.Message,), {
  'DESCRIPTOR' : _INSTANTIATECONTRACTPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.InstantiateContractProposal)
  })
_sym_db.RegisterMessage(InstantiateContractProposal)

MigrateContractProposal = _reflection.GeneratedProtocolMessageType('MigrateContractProposal', (_message.Message,), {
  'DESCRIPTOR' : _MIGRATECONTRACTPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.MigrateContractProposal)
  })
_sym_db.RegisterMessage(MigrateContractProposal)

SudoContractProposal = _reflection.GeneratedProtocolMessageType('SudoContractProposal', (_message.Message,), {
  'DESCRIPTOR' : _SUDOCONTRACTPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.SudoContractProposal)
  })
_sym_db.RegisterMessage(SudoContractProposal)

ExecuteContractProposal = _reflection.GeneratedProtocolMessageType('ExecuteContractProposal', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTECONTRACTPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.ExecuteContractProposal)
  })
_sym_db.RegisterMessage(ExecuteContractProposal)

UpdateAdminProposal = _reflection.GeneratedProtocolMessageType('UpdateAdminProposal', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEADMINPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.UpdateAdminProposal)
  })
_sym_db.RegisterMessage(UpdateAdminProposal)

ClearAdminProposal = _reflection.GeneratedProtocolMessageType('ClearAdminProposal', (_message.Message,), {
  'DESCRIPTOR' : _CLEARADMINPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.ClearAdminProposal)
  })
_sym_db.RegisterMessage(ClearAdminProposal)

PinCodesProposal = _reflection.GeneratedProtocolMessageType('PinCodesProposal', (_message.Message,), {
  'DESCRIPTOR' : _PINCODESPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.PinCodesProposal)
  })
_sym_db.RegisterMessage(PinCodesProposal)

UnpinCodesProposal = _reflection.GeneratedProtocolMessageType('UnpinCodesProposal', (_message.Message,), {
  'DESCRIPTOR' : _UNPINCODESPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.UnpinCodesProposal)
  })
_sym_db.RegisterMessage(UnpinCodesProposal)

AccessConfigUpdate = _reflection.GeneratedProtocolMessageType('AccessConfigUpdate', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSCONFIGUPDATE,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.AccessConfigUpdate)
  })
_sym_db.RegisterMessage(AccessConfigUpdate)

UpdateInstantiateConfigProposal = _reflection.GeneratedProtocolMessageType('UpdateInstantiateConfigProposal', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEINSTANTIATECONFIGPROPOSAL,
  '__module__' : 'cosmwasm.wasm.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.UpdateInstantiateConfigProposal)
  })
_sym_db.RegisterMessage(UpdateInstantiateConfigProposal)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\330\341\036\000\310\341\036\000\250\342\036\001'
  _STORECODEPROPOSAL.fields_by_name['wasm_byte_code']._options = None
  _STORECODEPROPOSAL.fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _INSTANTIATECONTRACTPROPOSAL.fields_by_name['code_id']._options = None
  _INSTANTIATECONTRACTPROPOSAL.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _INSTANTIATECONTRACTPROPOSAL.fields_by_name['msg']._options = None
  _INSTANTIATECONTRACTPROPOSAL.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _INSTANTIATECONTRACTPROPOSAL.fields_by_name['funds']._options = None
  _INSTANTIATECONTRACTPROPOSAL.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MIGRATECONTRACTPROPOSAL.fields_by_name['code_id']._options = None
  _MIGRATECONTRACTPROPOSAL.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MIGRATECONTRACTPROPOSAL.fields_by_name['msg']._options = None
  _MIGRATECONTRACTPROPOSAL.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _SUDOCONTRACTPROPOSAL.fields_by_name['msg']._options = None
  _SUDOCONTRACTPROPOSAL.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _EXECUTECONTRACTPROPOSAL.fields_by_name['msg']._options = None
  _EXECUTECONTRACTPROPOSAL.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _EXECUTECONTRACTPROPOSAL.fields_by_name['funds']._options = None
  _EXECUTECONTRACTPROPOSAL.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _UPDATEADMINPROPOSAL.fields_by_name['new_admin']._options = None
  _UPDATEADMINPROPOSAL.fields_by_name['new_admin']._serialized_options = b'\362\336\037\020yaml:\"new_admin\"'
  _PINCODESPROPOSAL.fields_by_name['title']._options = None
  _PINCODESPROPOSAL.fields_by_name['title']._serialized_options = b'\362\336\037\014yaml:\"title\"'
  _PINCODESPROPOSAL.fields_by_name['description']._options = None
  _PINCODESPROPOSAL.fields_by_name['description']._serialized_options = b'\362\336\037\022yaml:\"description\"'
  _PINCODESPROPOSAL.fields_by_name['code_ids']._options = None
  _PINCODESPROPOSAL.fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _UNPINCODESPROPOSAL.fields_by_name['title']._options = None
  _UNPINCODESPROPOSAL.fields_by_name['title']._serialized_options = b'\362\336\037\014yaml:\"title\"'
  _UNPINCODESPROPOSAL.fields_by_name['description']._options = None
  _UNPINCODESPROPOSAL.fields_by_name['description']._serialized_options = b'\362\336\037\022yaml:\"description\"'
  _UNPINCODESPROPOSAL.fields_by_name['code_ids']._options = None
  _UNPINCODESPROPOSAL.fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _ACCESSCONFIGUPDATE.fields_by_name['code_id']._options = None
  _ACCESSCONFIGUPDATE.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _ACCESSCONFIGUPDATE.fields_by_name['instantiate_permission']._options = None
  _ACCESSCONFIGUPDATE.fields_by_name['instantiate_permission']._serialized_options = b'\310\336\037\000'
  _UPDATEINSTANTIATECONFIGPROPOSAL.fields_by_name['title']._options = None
  _UPDATEINSTANTIATECONFIGPROPOSAL.fields_by_name['title']._serialized_options = b'\362\336\037\014yaml:\"title\"'
  _UPDATEINSTANTIATECONFIGPROPOSAL.fields_by_name['description']._options = None
  _UPDATEINSTANTIATECONFIGPROPOSAL.fields_by_name['description']._serialized_options = b'\362\336\037\022yaml:\"description\"'
  _UPDATEINSTANTIATECONFIGPROPOSAL.fields_by_name['access_config_updates']._options = None
  _UPDATEINSTANTIATECONFIGPROPOSAL.fields_by_name['access_config_updates']._serialized_options = b'\310\336\037\000'
  _STORECODEPROPOSAL._serialized_start=138
  _STORECODEPROPOSAL._serialized_end=327
  _INSTANTIATECONTRACTPROPOSAL._serialized_start=330
  _INSTANTIATECONTRACTPROPOSAL._serialized_end=599
  _MIGRATECONTRACTPROPOSAL._serialized_start=602
  _MIGRATECONTRACTPROPOSAL._serialized_end=747
  _SUDOCONTRACTPROPOSAL._serialized_start=749
  _SUDOCONTRACTPROPOSAL._serialized_end=862
  _EXECUTECONTRACTPROPOSAL._serialized_start=865
  _EXECUTECONTRACTPROPOSAL._serialized_end=1089
  _UPDATEADMINPROPOSAL._serialized_start=1091
  _UPDATEADMINPROPOSAL._serialized_end=1207
  _CLEARADMINPROPOSAL._serialized_start=1209
  _CLEARADMINPROPOSAL._serialized_end=1283
  _PINCODESPROPOSAL._serialized_start=1286
  _PINCODESPROPOSAL._serialized_end=1432
  _UNPINCODESPROPOSAL._serialized_start=1435
  _UNPINCODESPROPOSAL._serialized_end=1583
  _ACCESSCONFIGUPDATE._serialized_start=1585
  _ACCESSCONFIGUPDATE._serialized_end=1704
  _UPDATEINSTANTIATECONFIGPROPOSAL._serialized_start=1707
  _UPDATEINSTANTIATECONFIGPROPOSAL._serialized_end=1893
# @@protoc_insertion_point(module_scope)
