# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: top_down_nested.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15top_down_nested.proto\"\x8e\x02\n\x04\x43ity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08zip_code\x18\x02 \x01(\t\x12#\n\x0c\x63ountry_name\x18\x03 \x01(\x0e\x32\r.City.Country\x1as\n\x06Street\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x04\x63ity\x18\x02 \x01(\x0b\x32\x05.City\x1a\x46\n\x08\x42uilding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\r\x12\x1c\n\x06street\x18\x03 \x01(\x0b\x32\x0c.City.Street\"L\n\x07\x43ountry\x12\x17\n\x13\x43OUNTRY_UNSPECIFIED\x10\x00\x12\x12\n\x0eUNITIED_STATES\x10\x01\x12\t\n\x05\x43HINA\x10\x02\x12\t\n\x05JAPAN\x10\x03\"e\n\x07\x41\x64\x64ress\x12\x13\n\x04\x63ity\x18\x01 \x01(\x0b\x32\x05.City\x12\x1c\n\x06street\x18\x02 \x01(\x0b\x32\x0c.City.Street\x12\'\n\x08\x62uilding\x18\x03 \x01(\x0b\x32\x15.City.Street.Buildingb\x06proto3')



_CITY = DESCRIPTOR.message_types_by_name['City']
_CITY_STREET = _CITY.nested_types_by_name['Street']
_CITY_STREET_BUILDING = _CITY_STREET.nested_types_by_name['Building']
_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_CITY_COUNTRY = _CITY.enum_types_by_name['Country']
City = _reflection.GeneratedProtocolMessageType('City', (_message.Message,), {

  'Street' : _reflection.GeneratedProtocolMessageType('Street', (_message.Message,), {

    'Building' : _reflection.GeneratedProtocolMessageType('Building', (_message.Message,), {
      'DESCRIPTOR' : _CITY_STREET_BUILDING,
      '__module__' : 'top_down_nested_pb2'
      # @@protoc_insertion_point(class_scope:City.Street.Building)
      })
    ,
    'DESCRIPTOR' : _CITY_STREET,
    '__module__' : 'top_down_nested_pb2'
    # @@protoc_insertion_point(class_scope:City.Street)
    })
  ,
  'DESCRIPTOR' : _CITY,
  '__module__' : 'top_down_nested_pb2'
  # @@protoc_insertion_point(class_scope:City)
  })
_sym_db.RegisterMessage(City)
_sym_db.RegisterMessage(City.Street)
_sym_db.RegisterMessage(City.Street.Building)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'top_down_nested_pb2'
  # @@protoc_insertion_point(class_scope:Address)
  })
_sym_db.RegisterMessage(Address)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CITY._serialized_start=26
  _CITY._serialized_end=296
  _CITY_STREET._serialized_start=103
  _CITY_STREET._serialized_end=218
  _CITY_STREET_BUILDING._serialized_start=148
  _CITY_STREET_BUILDING._serialized_end=218
  _CITY_COUNTRY._serialized_start=220
  _CITY_COUNTRY._serialized_end=296
  _ADDRESS._serialized_start=298
  _ADDRESS._serialized_end=399
# @@protoc_insertion_point(module_scope)