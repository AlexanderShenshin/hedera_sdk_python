# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: auxiliary/tss/tss_share_signature.proto
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
    'auxiliary/tss/tss_share_signature.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'auxiliary/tss/tss_share_signature.proto\x12&com.hedera.hapi.services.auxiliary.tss\"{\n TssShareSignatureTransactionBody\x12\x13\n\x0broster_hash\x18\x01 \x01(\x0c\x12\x13\n\x0bshare_index\x18\x02 \x01(\x04\x12\x14\n\x0cmessage_hash\x18\x03 \x01(\x0c\x12\x17\n\x0fshare_signature\x18\x04 \x01(\x0c\x42\x31\n-com.hedera.hapi.services.auxiliary.tss.legacyP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auxiliary.tss.tss_share_signature_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n-com.hedera.hapi.services.auxiliary.tss.legacyP\001'
  _globals['_TSSSHARESIGNATURETRANSACTIONBODY']._serialized_start=83
  _globals['_TSSSHARESIGNATURETRANSACTIONBODY']._serialized_end=206
# @@protoc_insertion_point(module_scope)
