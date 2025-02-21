# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: consensus_service.proto
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
    'consensus_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hiero_sdk_python.hapi.services.basic_types_pb2 as basic__types__pb2
import hiero_sdk_python.hapi.services.timestamp_pb2 as timestamp__pb2
import hiero_sdk_python.hapi.services.consensus_submit_message_pb2 as consensus__submit__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63onsensus_service.proto\x12\x1b\x63om.hedera.mirror.api.proto\x1a\x11\x62\x61sic_types.proto\x1a\x0ftimestamp.proto\x1a\x1e\x63onsensus_submit_message.proto\"\x9f\x01\n\x13\x43onsensusTopicQuery\x12\x1f\n\x07topicID\x18\x01 \x01(\x0b\x32\x0e.proto.TopicID\x12,\n\x12\x63onsensusStartTime\x18\x02 \x01(\x0b\x32\x10.proto.Timestamp\x12*\n\x10\x63onsensusEndTime\x18\x03 \x01(\x0b\x32\x10.proto.Timestamp\x12\r\n\x05limit\x18\x04 \x01(\x04\"\xd5\x01\n\x16\x43onsensusTopicResponse\x12,\n\x12\x63onsensusTimestamp\x18\x01 \x01(\x0b\x32\x10.proto.Timestamp\x12\x0f\n\x07message\x18\x02 \x01(\x0c\x12\x13\n\x0brunningHash\x18\x03 \x01(\x0c\x12\x16\n\x0esequenceNumber\x18\x04 \x01(\x04\x12\x1a\n\x12runningHashVersion\x18\x05 \x01(\x04\x12\x33\n\tchunkInfo\x18\x06 \x01(\x0b\x32 .proto.ConsensusMessageChunkInfo2\x8d\x01\n\x10\x43onsensusService\x12y\n\x0esubscribeTopic\x12\x30.com.hedera.mirror.api.proto.ConsensusTopicQuery\x1a\x33.com.hedera.mirror.api.proto.ConsensusTopicResponse0\x01\x42\x1f\n\x1b\x63om.hedera.mirror.api.protoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'consensus_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hedera.mirror.api.protoP\001'
  _globals['_CONSENSUSTOPICQUERY']._serialized_start=125
  _globals['_CONSENSUSTOPICQUERY']._serialized_end=284
  _globals['_CONSENSUSTOPICRESPONSE']._serialized_start=287
  _globals['_CONSENSUSTOPICRESPONSE']._serialized_end=500
  _globals['_CONSENSUSSERVICE']._serialized_start=503
  _globals['_CONSENSUSSERVICE']._serialized_end=644
# @@protoc_insertion_point(module_scope)
