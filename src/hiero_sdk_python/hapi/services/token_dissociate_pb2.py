# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: token_dissociate.proto
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
    'token_dissociate.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16token_dissociate.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\"c\n\x1eTokenDissociateTransactionBody\x12!\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\x1e\n\x06tokens\x18\x02 \x03(\x0b\x32\x0e.proto.TokenIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'token_dissociate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_TOKENDISSOCIATETRANSACTIONBODY']._serialized_start=52
  _globals['_TOKENDISSOCIATETRANSACTIONBODY']._serialized_end=151
# @@protoc_insertion_point(module_scope)
