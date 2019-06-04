# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/v1/feature_config_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2
from kik_unofficial.protobuf.google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config/v1/feature_config_service.proto',
  package='mobile.config.v1',
  syntax='proto3',
  serialized_pb=_b('\n&config/v1/feature_config_service.proto\x12\x10mobile.config.v1\x1a\x19protobuf_validation.proto\x1a\x1egoogle/protobuf/duration.proto\"\x1a\n\x18GetFeatureConfigsRequest\"\xe5\x03\n\x19GetFeatureConfigsResponse\x12\x1c\n\x0emax_group_size\x18\n \x01(\rB\x04\xca\x9d%\x00\x12\x39\n1user_roster_entry_updates_legacy_roster_timestamp\x18\x0b \x01(\x08\x12/\n\'entity_service_get_trusted_bots_enabled\x18\x0c \x01(\x08\x12\x64\n9min_duration_between_pull_entity_service_get_trusted_bots\x18\r \x01(\x0b\x32\x19.google.protobuf.DurationB\x06\xca\x9d%\x02\x08\x01\x12\x1a\n\x12max_user_interests\x18\x0e \x01(\r\x12W\n\x1a\x63urrent_user_interest_list\x18\x0f \x03(\x0b\x32&.mobile.config.v1.UserInterestListItemB\x0b\xca\x9d%\x07\x08\x01x\x01\x80\x01\x64\x12U\n\x1a\x63urrent_chat_interest_list\x18\x10 \x03(\x0b\x32&.mobile.config.v1.ChatInterestListItemB\t\xca\x9d%\x05x\x01\x80\x01\x64J\x04\x08\x01\x10\x02R\x06result\">\n\x14UserInterestListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12localized_verbiage\x18\x02 \x01(\t\"]\n\x14\x43hatInterestListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12localized_interest\x18\x02 \x01(\t\x12\x1d\n\x15localized_ice_breaker\x18\x03 \x01(\t\"\x1e\n\x1cGetAllUserInterestIdsRequest\"9\n\x1dGetAllUserInterestIdsResponse\x12\x18\n\x03ids\x18\x01 \x03(\tB\x0b\xca\x9d%\x07\x08\x01x\x01\x80\x01\x64\"\x1c\n\x1aGetAllChatInterestsRequest\"j\n\x1bGetAllChatInterestsResponse\x12K\n\x0e\x63hat_interests\x18\x01 \x03(\x0b\x32&.mobile.config.v1.ChatInterestListItemB\x0b\xca\x9d%\x07\x08\x01x\x01\x80\x01\x64\x32\xf1\x02\n\rFeatureConfig\x12n\n\x11GetFeatureConfigs\x12*.mobile.config.v1.GetFeatureConfigsRequest\x1a+.mobile.config.v1.GetFeatureConfigsResponse\"\x00\x12z\n\x15GetAllUserInterestIds\x12..mobile.config.v1.GetAllUserInterestIdsRequest\x1a/.mobile.config.v1.GetAllUserInterestIdsResponse\"\x00\x12t\n\x13GetAllChatInterests\x12,.mobile.config.v1.GetAllChatInterestsRequest\x1a-.mobile.config.v1.GetAllChatInterestsResponse\"\x00\x42g\n\x19\x63om.kik.featureconfig.rpcZJgithub.com/kikinteractive/xiphias-api-mobile/generated/go/config/v1;configb\x06proto3')
  ,
  dependencies=[protobuf__validation__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETFEATURECONFIGSREQUEST = _descriptor.Descriptor(
  name='GetFeatureConfigsRequest',
  full_name='mobile.config.v1.GetFeatureConfigsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=119,
  serialized_end=145,
)


_GETFEATURECONFIGSRESPONSE = _descriptor.Descriptor(
  name='GetFeatureConfigsResponse',
  full_name='mobile.config.v1.GetFeatureConfigsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_group_size', full_name='mobile.config.v1.GetFeatureConfigsResponse.max_group_size', index=0,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\000'))),
    _descriptor.FieldDescriptor(
      name='user_roster_entry_updates_legacy_roster_timestamp', full_name='mobile.config.v1.GetFeatureConfigsResponse.user_roster_entry_updates_legacy_roster_timestamp', index=1,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entity_service_get_trusted_bots_enabled', full_name='mobile.config.v1.GetFeatureConfigsResponse.entity_service_get_trusted_bots_enabled', index=2,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_duration_between_pull_entity_service_get_trusted_bots', full_name='mobile.config.v1.GetFeatureConfigsResponse.min_duration_between_pull_entity_service_get_trusted_bots', index=3,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='max_user_interests', full_name='mobile.config.v1.GetFeatureConfigsResponse.max_user_interests', index=4,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_user_interest_list', full_name='mobile.config.v1.GetFeatureConfigsResponse.current_user_interest_list', index=5,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001d'))),
    _descriptor.FieldDescriptor(
      name='current_chat_interest_list', full_name='mobile.config.v1.GetFeatureConfigsResponse.current_chat_interest_list', index=6,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005x\001\200\001d'))),
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
  serialized_start=148,
  serialized_end=633,
)


_USERINTERESTLISTITEM = _descriptor.Descriptor(
  name='UserInterestListItem',
  full_name='mobile.config.v1.UserInterestListItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mobile.config.v1.UserInterestListItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localized_verbiage', full_name='mobile.config.v1.UserInterestListItem.localized_verbiage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=635,
  serialized_end=697,
)


_CHATINTERESTLISTITEM = _descriptor.Descriptor(
  name='ChatInterestListItem',
  full_name='mobile.config.v1.ChatInterestListItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mobile.config.v1.ChatInterestListItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localized_interest', full_name='mobile.config.v1.ChatInterestListItem.localized_interest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localized_ice_breaker', full_name='mobile.config.v1.ChatInterestListItem.localized_ice_breaker', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=699,
  serialized_end=792,
)


_GETALLUSERINTERESTIDSREQUEST = _descriptor.Descriptor(
  name='GetAllUserInterestIdsRequest',
  full_name='mobile.config.v1.GetAllUserInterestIdsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=794,
  serialized_end=824,
)


_GETALLUSERINTERESTIDSRESPONSE = _descriptor.Descriptor(
  name='GetAllUserInterestIdsResponse',
  full_name='mobile.config.v1.GetAllUserInterestIdsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='mobile.config.v1.GetAllUserInterestIdsResponse.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001d'))),
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
  serialized_start=826,
  serialized_end=883,
)


_GETALLCHATINTERESTSREQUEST = _descriptor.Descriptor(
  name='GetAllChatInterestsRequest',
  full_name='mobile.config.v1.GetAllChatInterestsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=885,
  serialized_end=913,
)


_GETALLCHATINTERESTSRESPONSE = _descriptor.Descriptor(
  name='GetAllChatInterestsResponse',
  full_name='mobile.config.v1.GetAllChatInterestsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chat_interests', full_name='mobile.config.v1.GetAllChatInterestsResponse.chat_interests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001d'))),
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
  serialized_start=915,
  serialized_end=1021,
)

_GETFEATURECONFIGSRESPONSE.fields_by_name['min_duration_between_pull_entity_service_get_trusted_bots'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_GETFEATURECONFIGSRESPONSE.fields_by_name['current_user_interest_list'].message_type = _USERINTERESTLISTITEM
_GETFEATURECONFIGSRESPONSE.fields_by_name['current_chat_interest_list'].message_type = _CHATINTERESTLISTITEM
_GETALLCHATINTERESTSRESPONSE.fields_by_name['chat_interests'].message_type = _CHATINTERESTLISTITEM
DESCRIPTOR.message_types_by_name['GetFeatureConfigsRequest'] = _GETFEATURECONFIGSREQUEST
DESCRIPTOR.message_types_by_name['GetFeatureConfigsResponse'] = _GETFEATURECONFIGSRESPONSE
DESCRIPTOR.message_types_by_name['UserInterestListItem'] = _USERINTERESTLISTITEM
DESCRIPTOR.message_types_by_name['ChatInterestListItem'] = _CHATINTERESTLISTITEM
DESCRIPTOR.message_types_by_name['GetAllUserInterestIdsRequest'] = _GETALLUSERINTERESTIDSREQUEST
DESCRIPTOR.message_types_by_name['GetAllUserInterestIdsResponse'] = _GETALLUSERINTERESTIDSRESPONSE
DESCRIPTOR.message_types_by_name['GetAllChatInterestsRequest'] = _GETALLCHATINTERESTSREQUEST
DESCRIPTOR.message_types_by_name['GetAllChatInterestsResponse'] = _GETALLCHATINTERESTSRESPONSE

GetFeatureConfigsRequest = _reflection.GeneratedProtocolMessageType('GetFeatureConfigsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATURECONFIGSREQUEST,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.GetFeatureConfigsRequest)
  ))
_sym_db.RegisterMessage(GetFeatureConfigsRequest)

GetFeatureConfigsResponse = _reflection.GeneratedProtocolMessageType('GetFeatureConfigsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFEATURECONFIGSRESPONSE,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.GetFeatureConfigsResponse)
  ))
_sym_db.RegisterMessage(GetFeatureConfigsResponse)

UserInterestListItem = _reflection.GeneratedProtocolMessageType('UserInterestListItem', (_message.Message,), dict(
  DESCRIPTOR = _USERINTERESTLISTITEM,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.UserInterestListItem)
  ))
_sym_db.RegisterMessage(UserInterestListItem)

ChatInterestListItem = _reflection.GeneratedProtocolMessageType('ChatInterestListItem', (_message.Message,), dict(
  DESCRIPTOR = _CHATINTERESTLISTITEM,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.ChatInterestListItem)
  ))
_sym_db.RegisterMessage(ChatInterestListItem)

GetAllUserInterestIdsRequest = _reflection.GeneratedProtocolMessageType('GetAllUserInterestIdsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETALLUSERINTERESTIDSREQUEST,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.GetAllUserInterestIdsRequest)
  ))
_sym_db.RegisterMessage(GetAllUserInterestIdsRequest)

GetAllUserInterestIdsResponse = _reflection.GeneratedProtocolMessageType('GetAllUserInterestIdsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALLUSERINTERESTIDSRESPONSE,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.GetAllUserInterestIdsResponse)
  ))
_sym_db.RegisterMessage(GetAllUserInterestIdsResponse)

GetAllChatInterestsRequest = _reflection.GeneratedProtocolMessageType('GetAllChatInterestsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETALLCHATINTERESTSREQUEST,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.GetAllChatInterestsRequest)
  ))
_sym_db.RegisterMessage(GetAllChatInterestsRequest)

GetAllChatInterestsResponse = _reflection.GeneratedProtocolMessageType('GetAllChatInterestsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALLCHATINTERESTSRESPONSE,
  __module__ = 'config.v1.feature_config_service_pb2'
  # @@protoc_insertion_point(class_scope:mobile.config.v1.GetAllChatInterestsResponse)
  ))
_sym_db.RegisterMessage(GetAllChatInterestsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\031com.kik.featureconfig.rpcZJgithub.com/kikinteractive/xiphias-api-mobile/generated/go/config/v1;config'))
_GETFEATURECONFIGSRESPONSE.fields_by_name['max_group_size'].has_options = True
_GETFEATURECONFIGSRESPONSE.fields_by_name['max_group_size']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\000'))
_GETFEATURECONFIGSRESPONSE.fields_by_name['min_duration_between_pull_entity_service_get_trusted_bots'].has_options = True
_GETFEATURECONFIGSRESPONSE.fields_by_name['min_duration_between_pull_entity_service_get_trusted_bots']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\002\010\001'))
_GETFEATURECONFIGSRESPONSE.fields_by_name['current_user_interest_list'].has_options = True
_GETFEATURECONFIGSRESPONSE.fields_by_name['current_user_interest_list']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001d'))
_GETFEATURECONFIGSRESPONSE.fields_by_name['current_chat_interest_list'].has_options = True
_GETFEATURECONFIGSRESPONSE.fields_by_name['current_chat_interest_list']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\005x\001\200\001d'))
_GETALLUSERINTERESTIDSRESPONSE.fields_by_name['ids'].has_options = True
_GETALLUSERINTERESTIDSRESPONSE.fields_by_name['ids']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001d'))
_GETALLCHATINTERESTSRESPONSE.fields_by_name['chat_interests'].has_options = True
_GETALLCHATINTERESTSRESPONSE.fields_by_name['chat_interests']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\312\235%\007\010\001x\001\200\001d'))
# @@protoc_insertion_point(module_scope)