# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: crypto_service.proto
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
    'crypto_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import query_pb2 as query__pb2
from . import response_pb2 as response__pb2
from . import transaction_response_pb2 as transaction__response__pb2
from . import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63rypto_service.proto\x12\x05proto\x1a\x0bquery.proto\x1a\x0eresponse.proto\x1a\x1atransaction_response.proto\x1a\x11transaction.proto2\xc3\x07\n\rCryptoService\x12?\n\rcreateAccount\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12?\n\rupdateAccount\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12@\n\x0e\x63ryptoTransfer\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12>\n\x0c\x63ryptoDelete\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x43\n\x11\x61pproveAllowances\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12\x42\n\x10\x64\x65leteAllowances\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12=\n\x0b\x61\x64\x64LiveHash\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12@\n\x0e\x64\x65leteLiveHash\x12\x12.proto.Transaction\x1a\x1a.proto.TransactionResponse\x12,\n\x0bgetLiveHash\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x32\n\x11getAccountRecords\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x31\n\x10\x63ryptoGetBalance\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12/\n\x0egetAccountInfo\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x37\n\x16getTransactionReceipts\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x39\n\x18getFastTransactionRecord\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x32\n\x11getTxRecordByTxID\x12\x0c.proto.Query\x1a\x0f.proto.Response\x12\x36\n\x15getStakersByAccountID\x12\x0c.proto.Query\x1a\x0f.proto.ResponseB(\n&com.hederahashgraph.service.proto.javab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crypto_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.hederahashgraph.service.proto.java'
  _globals['_CRYPTOSERVICE']._serialized_start=108
  _globals['_CRYPTOSERVICE']._serialized_end=1071
# @@protoc_insertion_point(module_scope)
