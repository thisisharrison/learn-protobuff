# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import city_pb2 as city__pb2
import street_pb2 as street__pb2
import building_pb2 as building__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\raddress.proto\x1a\ncity.proto\x1a\x0cstreet.proto\x1a\x0e\x62uilding.proto\"^\n\x07\x41\x64\x64ress\x12\x13\n\x04\x63ity\x18\x01 \x01(\x0b\x32\x05.City\x12!\n\x06street\x18\x02 \x01(\x0b\x32\x11.my.street.Street\x12\x1b\n\x08\x62uilding\x18\x03 \x01(\x0b\x32\t.Buildingb\x06proto3')



_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'address_pb2'
  # @@protoc_insertion_point(class_scope:Address)
  })
_sym_db.RegisterMessage(Address)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDRESS._serialized_start=59
  _ADDRESS._serialized_end=153
# @@protoc_insertion_point(module_scope)
