# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  serialized_pb='\n\x0emessages.proto\"L\n\x04User\x12\x0b\n\x03\x61ge\x18\x01 \x02(\x05\x12\x12\n\ndepartment\x18\x02 \x02(\t\x12\x0e\n\x06\x64\x65gree\x18\x03 \x02(\t\x12\x13\n\x0b\x64\x65gree_year\x18\x04 \x02(\t\"*\n\x08MobileOS\x12\n\n\x02os\x18\x01 \x02(\t\x12\x12\n\nos_version\x18\x02 \x02(\t\"x\n\x0cMobileDevice\x12\r\n\x05\x62rand\x18\x01 \x02(\t\x12\r\n\x05model\x18\x02 \x02(\t\x12\x15\n\raudio_support\x18\x03 \x02(\x08\x12\x15\n\rvideo_support\x18\x04 \x02(\x08\x12\x1c\n\tmobile_os\x18\x05 \x02(\x0b\x32\t.MobileOS\"/\n\x0eNetworkDetails\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x11\n\tbandwidth\x18\x02 \x02(\x01\"\"\n\x06RSAKey\x12\x0b\n\x03mod\x18\x01 \x02(\t\x12\x0b\n\x03\x65xp\x18\x02 \x02(\t\"\xb9\x01\n\x0cRegisterUser\x12\x10\n\x08username\x18\x01 \x02(\t\x12\x13\n\x04user\x18\x02 \x02(\x0b\x32\x05.User\x12$\n\rmobile_device\x18\x03 \x02(\x0b\x32\r.MobileDevice\x12(\n\x0fnetwork_details\x18\x04 \x02(\x0b\x32\x0f.NetworkDetails\x12\x1b\n\npublic_key\x18\x05 \x02(\x0b\x32\x07.RSAKey\x12\x15\n\rsymmetric_key\x18\x06 \x02(\t\" \n\x0cGetPublicKey\x12\x10\n\x08username\x18\x01 \x02(\t\"3\n\x14GetPublicKeyResponse\x12\x1b\n\npublic_key\x18\x01 \x02(\x0b\x32\x07.RSAKey\"\'\n\x14RegisterUserResponse\x12\x0f\n\x07user_id\x18\x01 \x02(\x03\"+\n\tSendQuery\x12\x0f\n\x07user_id\x18\x01 \x02(\x03\x12\r\n\x05query\x18\x02 \x02(\t\"7\n\x11SendQueryResponse\x12\"\n\x0cquery_result\x18\x01 \x03(\x0b\x32\x0c.QueryResult\")\n\x0bQueryResult\x12\r\n\x05title\x18\x01 \x02(\t\x12\x0b\n\x03url\x18\x02 \x02(\t')




_USER = descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='age', full_name='User.age', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='department', full_name='User.department', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='degree', full_name='User.degree', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='degree_year', full_name='User.degree_year', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=18,
  serialized_end=94,
)


_MOBILEOS = descriptor.Descriptor(
  name='MobileOS',
  full_name='MobileOS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='os', full_name='MobileOS.os', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='os_version', full_name='MobileOS.os_version', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=96,
  serialized_end=138,
)


_MOBILEDEVICE = descriptor.Descriptor(
  name='MobileDevice',
  full_name='MobileDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='brand', full_name='MobileDevice.brand', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='model', full_name='MobileDevice.model', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='audio_support', full_name='MobileDevice.audio_support', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='video_support', full_name='MobileDevice.video_support', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mobile_os', full_name='MobileDevice.mobile_os', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=140,
  serialized_end=260,
)


_NETWORKDETAILS = descriptor.Descriptor(
  name='NetworkDetails',
  full_name='NetworkDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ip', full_name='NetworkDetails.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bandwidth', full_name='NetworkDetails.bandwidth', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=262,
  serialized_end=309,
)


_RSAKEY = descriptor.Descriptor(
  name='RSAKey',
  full_name='RSAKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mod', full_name='RSAKey.mod', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exp', full_name='RSAKey.exp', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=311,
  serialized_end=345,
)


_REGISTERUSER = descriptor.Descriptor(
  name='RegisterUser',
  full_name='RegisterUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='username', full_name='RegisterUser.username', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='RegisterUser.user', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mobile_device', full_name='RegisterUser.mobile_device', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='network_details', full_name='RegisterUser.network_details', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='public_key', full_name='RegisterUser.public_key', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='symmetric_key', full_name='RegisterUser.symmetric_key', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=348,
  serialized_end=533,
)


_GETPUBLICKEY = descriptor.Descriptor(
  name='GetPublicKey',
  full_name='GetPublicKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='username', full_name='GetPublicKey.username', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=535,
  serialized_end=567,
)


_GETPUBLICKEYRESPONSE = descriptor.Descriptor(
  name='GetPublicKeyResponse',
  full_name='GetPublicKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='public_key', full_name='GetPublicKeyResponse.public_key', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=569,
  serialized_end=620,
)


_REGISTERUSERRESPONSE = descriptor.Descriptor(
  name='RegisterUserResponse',
  full_name='RegisterUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user_id', full_name='RegisterUserResponse.user_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=622,
  serialized_end=661,
)


_SENDQUERY = descriptor.Descriptor(
  name='SendQuery',
  full_name='SendQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user_id', full_name='SendQuery.user_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='query', full_name='SendQuery.query', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=663,
  serialized_end=706,
)


_SENDQUERYRESPONSE = descriptor.Descriptor(
  name='SendQueryResponse',
  full_name='SendQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='query_result', full_name='SendQueryResponse.query_result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=708,
  serialized_end=763,
)


_QUERYRESULT = descriptor.Descriptor(
  name='QueryResult',
  full_name='QueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='title', full_name='QueryResult.title', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url', full_name='QueryResult.url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=765,
  serialized_end=806,
)

_MOBILEDEVICE.fields_by_name['mobile_os'].message_type = _MOBILEOS
_REGISTERUSER.fields_by_name['user'].message_type = _USER
_REGISTERUSER.fields_by_name['mobile_device'].message_type = _MOBILEDEVICE
_REGISTERUSER.fields_by_name['network_details'].message_type = _NETWORKDETAILS
_REGISTERUSER.fields_by_name['public_key'].message_type = _RSAKEY
_GETPUBLICKEYRESPONSE.fields_by_name['public_key'].message_type = _RSAKEY
_SENDQUERYRESPONSE.fields_by_name['query_result'].message_type = _QUERYRESULT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['MobileOS'] = _MOBILEOS
DESCRIPTOR.message_types_by_name['MobileDevice'] = _MOBILEDEVICE
DESCRIPTOR.message_types_by_name['NetworkDetails'] = _NETWORKDETAILS
DESCRIPTOR.message_types_by_name['RSAKey'] = _RSAKEY
DESCRIPTOR.message_types_by_name['RegisterUser'] = _REGISTERUSER
DESCRIPTOR.message_types_by_name['GetPublicKey'] = _GETPUBLICKEY
DESCRIPTOR.message_types_by_name['GetPublicKeyResponse'] = _GETPUBLICKEYRESPONSE
DESCRIPTOR.message_types_by_name['RegisterUserResponse'] = _REGISTERUSERRESPONSE
DESCRIPTOR.message_types_by_name['SendQuery'] = _SENDQUERY
DESCRIPTOR.message_types_by_name['SendQueryResponse'] = _SENDQUERYRESPONSE
DESCRIPTOR.message_types_by_name['QueryResult'] = _QUERYRESULT

class User(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USER
  
  # @@protoc_insertion_point(class_scope:User)

class MobileOS(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MOBILEOS
  
  # @@protoc_insertion_point(class_scope:MobileOS)

class MobileDevice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MOBILEDEVICE
  
  # @@protoc_insertion_point(class_scope:MobileDevice)

class NetworkDetails(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NETWORKDETAILS
  
  # @@protoc_insertion_point(class_scope:NetworkDetails)

class RSAKey(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSAKEY
  
  # @@protoc_insertion_point(class_scope:RSAKey)

class RegisterUser(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERUSER
  
  # @@protoc_insertion_point(class_scope:RegisterUser)

class GetPublicKey(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPUBLICKEY
  
  # @@protoc_insertion_point(class_scope:GetPublicKey)

class GetPublicKeyResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPUBLICKEYRESPONSE
  
  # @@protoc_insertion_point(class_scope:GetPublicKeyResponse)

class RegisterUserResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERUSERRESPONSE
  
  # @@protoc_insertion_point(class_scope:RegisterUserResponse)

class SendQuery(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SENDQUERY
  
  # @@protoc_insertion_point(class_scope:SendQuery)

class SendQueryResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SENDQUERYRESPONSE
  
  # @@protoc_insertion_point(class_scope:SendQueryResponse)

class QueryResult(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYRESULT
  
  # @@protoc_insertion_point(class_scope:QueryResult)

# @@protoc_insertion_point(module_scope)