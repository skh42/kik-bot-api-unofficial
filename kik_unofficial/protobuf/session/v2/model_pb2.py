# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session/v2/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kik_unofficial.protobuf.google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='session/v2/model.proto',
  package='common.session.v2',
  syntax='proto3',
  serialized_pb=_b('\n\x16session/v2/model.proto\x12\x11\x63ommon.session.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8c\x01\n\x0cSessionToken\x12\x34\n\x05token\x18\x01 \x01(\x0b\x32%.common.session.v2.SessionToken.Token\x12*\n\x06\x65xpiry\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x1a\n\x05Token\x12\x11\n\traw_value\x18\x01 \x01(\x0c\x42}\n\x16\x63om.kik.gen.session.v2ZNgithub.com/kikinteractive/xiphias-model-common/generated/go/session/v2;session\xa2\x02\x12KPBCommonSessionV2b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SESSIONTOKEN_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='common.session.v2.SessionToken.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='common.session.v2.SessionToken.Token.raw_value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=219,
)

_SESSIONTOKEN = _descriptor.Descriptor(
  name='SessionToken',
  full_name='common.session.v2.SessionToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='common.session.v2.SessionToken.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='common.session.v2.SessionToken.expiry', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SESSIONTOKEN_TOKEN, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=219,
)

_SESSIONTOKEN_TOKEN.containing_type = _SESSIONTOKEN
_SESSIONTOKEN.fields_by_name['token'].message_type = _SESSIONTOKEN_TOKEN
_SESSIONTOKEN.fields_by_name['expiry'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['SessionToken'] = _SESSIONTOKEN

SessionToken = _reflection.GeneratedProtocolMessageType('SessionToken', (_message.Message,), dict(

  Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), dict(
    DESCRIPTOR = _SESSIONTOKEN_TOKEN,
    __module__ = 'session.v2.model_pb2'
    # @@protoc_insertion_point(class_scope:common.session.v2.SessionToken.Token)
    ))
  ,
  DESCRIPTOR = _SESSIONTOKEN,
  __module__ = 'session.v2.model_pb2'
  # @@protoc_insertion_point(class_scope:common.session.v2.SessionToken)
  ))
_sym_db.RegisterMessage(SessionToken)
_sym_db.RegisterMessage(SessionToken.Token)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.kik.gen.session.v2ZNgithub.com/kikinteractive/xiphias-model-common/generated/go/session/v2;session\242\002\022KPBCommonSessionV2'))
# @@protoc_insertion_point(module_scope)