# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: freeze.proto
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
    'freeze.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import timestamp_pb2 as timestamp__pb2
from . import basic_types_pb2 as basic__types__pb2
from . import freeze_type_pb2 as freeze__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x66reeze.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x11\x62\x61sic_types.proto\x1a\x11\x66reeze_type.proto\"\xf2\x01\n\x15\x46reezeTransactionBody\x12\x15\n\tstartHour\x18\x01 \x01(\x05\x42\x02\x18\x01\x12\x14\n\x08startMin\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x13\n\x07\x65ndHour\x18\x03 \x01(\x05\x42\x02\x18\x01\x12\x12\n\x06\x65ndMin\x18\x04 \x01(\x05\x42\x02\x18\x01\x12\"\n\x0bupdate_file\x18\x05 \x01(\x0b\x32\r.proto.FileID\x12\x11\n\tfile_hash\x18\x06 \x01(\x0c\x12$\n\nstart_time\x18\x07 \x01(\x0b\x32\x10.proto.Timestamp\x12&\n\x0b\x66reeze_type\x18\x08 \x01(\x0e\x32\x11.proto.FreezeTypeB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'freeze_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['startHour']._loaded_options = None
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['startHour']._serialized_options = b'\030\001'
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['startMin']._loaded_options = None
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['startMin']._serialized_options = b'\030\001'
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['endHour']._loaded_options = None
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['endHour']._serialized_options = b'\030\001'
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['endMin']._loaded_options = None
  _globals['_FREEZETRANSACTIONBODY'].fields_by_name['endMin']._serialized_options = b'\030\001'
  _globals['_FREEZETRANSACTIONBODY']._serialized_start=79
  _globals['_FREEZETRANSACTIONBODY']._serialized_end=321
# @@protoc_insertion_point(module_scope)
