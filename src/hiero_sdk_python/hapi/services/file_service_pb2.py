# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: file_service.proto
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
    'file_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import query_pb2 as query__pb2
from . import response_pb2 as response__pb2
from . import transaction_response_pb2 as transaction__response__pb2
from . import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66ile_service.proto\x12\x05proto\x1a\x0bquery.proto\x1a\x0eresponse.proto\x1a\x1atransaction_response.proto\x1a\x11transaction.proto2\xe9\x03\n\x0b\x46ileService\x12<\n\ncreateFile\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12<\n\nupdateFile\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12<\n\ndeleteFile\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12?\n\rappendContent\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12/\n\x0egetFileContent\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12,\n\x0bgetFileInfo\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12>\n\x0csystemDelete\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12@\n\x0esystemUndelete\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponseB(\n&com.hederahashgraph.service.proto.javab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.hederahashgraph.service.proto.java'
  _globals['_FILESERVICE']._serialized_start=106
  _globals['_FILESERVICE']._serialized_end=595
# @@protoc_insertion_point(module_scope)
