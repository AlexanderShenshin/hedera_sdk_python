# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event/gossip_event.proto
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
    'event/gossip_event.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .event import event_transaction_pb2 as event_dot_event__transaction__pb2
from .event import event_core_pb2 as event_dot_event__core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x65vent/gossip_event.proto\x12\x1e\x63om.hedera.hapi.platform.event\x1a\x1d\x65vent/event_transaction.proto\x1a\x16\x65vent/event_core.proto\"\xc6\x01\n\x0bGossipEvent\x12=\n\nevent_core\x18\x01 \x01(\x0b\x32).com.hedera.hapi.platform.event.EventCore\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12O\n\x11\x65vent_transaction\x18\x03 \x03(\x0b\x32\x30.com.hedera.hapi.platform.event.EventTransactionB\x02\x18\x01\x12\x14\n\x0ctransactions\x18\x04 \x03(\x0c\x42)\n%com.hedera.hapi.platform.event.legacyP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event.gossip_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.hedera.hapi.platform.event.legacyP\001'
  _globals['_GOSSIPEVENT'].fields_by_name['event_transaction']._loaded_options = None
  _globals['_GOSSIPEVENT'].fields_by_name['event_transaction']._serialized_options = b'\030\001'
  _globals['_GOSSIPEVENT']._serialized_start=116
  _globals['_GOSSIPEVENT']._serialized_end=314
# @@protoc_insertion_point(module_scope)
