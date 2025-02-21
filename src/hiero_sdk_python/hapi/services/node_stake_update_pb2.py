# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: node_stake_update.proto
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
    'node_stake_update.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2
from . import timestamp_pb2 as timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17node_stake_update.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0ftimestamp.proto\"\xa9\x04\n\x1eNodeStakeUpdateTransactionBody\x12/\n\x15\x65nd_of_staking_period\x18\x01 \x01(\x0b\x32\x10.proto.Timestamp\x12$\n\nnode_stake\x18\x02 \x03(\x0b\x32\x10.proto.NodeStake\x12(\n max_staking_reward_rate_per_hbar\x18\x03 \x01(\x03\x12\x31\n\x18node_reward_fee_fraction\x18\x04 \x01(\x0b\x32\x0f.proto.Fraction\x12\x1e\n\x16staking_periods_stored\x18\x05 \x01(\x03\x12\x16\n\x0estaking_period\x18\x06 \x01(\x03\x12\x34\n\x1bstaking_reward_fee_fraction\x18\x07 \x01(\x0b\x32\x0f.proto.Fraction\x12\x1f\n\x17staking_start_threshold\x18\x08 \x01(\x03\x12\x1f\n\x13staking_reward_rate\x18\t \x01(\x03\x42\x02\x18\x01\x12 \n\x18reserved_staking_rewards\x18\n \x01(\x03\x12)\n!unreserved_staking_reward_balance\x18\x0b \x01(\x03\x12 \n\x18reward_balance_threshold\x18\x0c \x01(\x03\x12\x1a\n\x12max_stake_rewarded\x18\r \x01(\x03\x12\x18\n\x10max_total_reward\x18\x0e \x01(\x03\"\x9a\x01\n\tNodeStake\x12\x11\n\tmax_stake\x18\x01 \x01(\x03\x12\x11\n\tmin_stake\x18\x02 \x01(\x03\x12\x0f\n\x07node_id\x18\x03 \x01(\x03\x12\x13\n\x0breward_rate\x18\x04 \x01(\x03\x12\r\n\x05stake\x18\x05 \x01(\x03\x12\x1a\n\x12stake_not_rewarded\x18\x06 \x01(\x03\x12\x16\n\x0estake_rewarded\x18\x07 \x01(\x03\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'node_stake_update_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_NODESTAKEUPDATETRANSACTIONBODY'].fields_by_name['staking_reward_rate']._loaded_options = None
  _globals['_NODESTAKEUPDATETRANSACTIONBODY'].fields_by_name['staking_reward_rate']._serialized_options = b'\030\001'
  _globals['_NODESTAKEUPDATETRANSACTIONBODY']._serialized_start=71
  _globals['_NODESTAKEUPDATETRANSACTIONBODY']._serialized_end=624
  _globals['_NODESTAKE']._serialized_start=627
  _globals['_NODESTAKE']._serialized_end=781
# @@protoc_insertion_point(module_scope)
