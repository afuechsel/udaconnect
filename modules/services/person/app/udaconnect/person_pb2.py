# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cperson.proto\"X\n\rPersonMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"\x07\n\x05\x45mpty\"4\n\x11PersonMessageList\x12\x1f\n\x07persons\x18\x01 \x03(\x0b\x32\x0e.PersonMessage22\n\rPersonService\x12!\n\x03Get\x12\x06.Empty\x1a\x12.PersonMessageListb\x06proto3')



_PERSONMESSAGE = DESCRIPTOR.message_types_by_name['PersonMessage']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_PERSONMESSAGELIST = DESCRIPTOR.message_types_by_name['PersonMessageList']
PersonMessage = _reflection.GeneratedProtocolMessageType('PersonMessage', (_message.Message,), {
  'DESCRIPTOR' : _PERSONMESSAGE,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:PersonMessage)
  })
_sym_db.RegisterMessage(PersonMessage)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

PersonMessageList = _reflection.GeneratedProtocolMessageType('PersonMessageList', (_message.Message,), {
  'DESCRIPTOR' : _PERSONMESSAGELIST,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:PersonMessageList)
  })
_sym_db.RegisterMessage(PersonMessageList)

_PERSONSERVICE = DESCRIPTOR.services_by_name['PersonService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERSONMESSAGE._serialized_start=16
  _PERSONMESSAGE._serialized_end=104
  _EMPTY._serialized_start=106
  _EMPTY._serialized_end=113
  _PERSONMESSAGELIST._serialized_start=115
  _PERSONMESSAGELIST._serialized_end=167
  _PERSONSERVICE._serialized_start=169
  _PERSONSERVICE._serialized_end=219
# @@protoc_insertion_point(module_scope)
