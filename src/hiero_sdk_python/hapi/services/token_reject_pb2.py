# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: token_reject.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'token_reject.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12token_reject.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"h\n\x1aTokenRejectTransactionBody\x12\x1f\n\x05owner\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12)\n\nrejections\x18\x02 \x03(\x0b\x32\x15.proto.TokenReference\"k\n\x0eTokenReference\x12(\n\x0e\x66ungible_token\x18\x01 \x01(\x0b\x32\x0e.proto.TokenIDH\x00\x12\x1b\n\x03nft\x18\x02 \x01(\x0b\x32\x0c.proto.NftIDH\x00\x42\x12\n\x10token_identifierB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'token_reject_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_TOKENREJECTTRANSACTIONBODY']._serialized_start=48
  _globals['_TOKENREJECTTRANSACTIONBODY']._serialized_end=152
  _globals['_TOKENREFERENCE']._serialized_start=154
  _globals['_TOKENREFERENCE']._serialized_end=261
# @@protoc_insertion_point(module_scope)
