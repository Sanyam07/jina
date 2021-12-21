# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jina.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import docarray.proto.docarray_pb2 as docarray__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\njina.proto\x12\x04jina\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0e\x64ocarray.proto\"\x9a\x01\n\nRouteProto\x12\x0b\n\x03pod\x18\x01 \x01(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12!\n\x06status\x18\x04 \x01(\x0b\x32\x11.jina.StatusProto\"\xc2\x01\n\x0bHeaderProto\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12!\n\x06status\x18\x02 \x01(\x0b\x32\x11.jina.StatusProto\x12\x1a\n\rexec_endpoint\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rtarget_peapod\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07timeout\x18\x05 \x01(\rH\x02\x88\x01\x01\x42\x10\n\x0e_exec_endpointB\x10\n\x0e_target_peapodB\n\n\x08_timeout\"\xcf\x02\n\x0bStatusProto\x12*\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1c.jina.StatusProto.StatusCode\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x33\n\texception\x18\x03 \x01(\x0b\x32 .jina.StatusProto.ExceptionProto\x1aN\n\x0e\x45xceptionProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\x12\x0e\n\x06stacks\x18\x03 \x03(\t\x12\x10\n\x08\x65xecutor\x18\x04 \x01(\t\"z\n\nStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\t\n\x05READY\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x13\n\x0f\x45RROR_DUPLICATE\x10\x04\x12\x14\n\x10\x45RROR_NOTALLOWED\x10\x05\x12\x11\n\rERROR_CHAINED\x10\x06\"^\n\rRelatedEntity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\x12\x15\n\x08shard_id\x18\x04 \x01(\rH\x00\x88\x01\x01\x42\x0b\n\t_shard_id\"\xcf\x01\n\x13\x43ontrolRequestProto\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.jina.HeaderProto\x12\x32\n\x07\x63ommand\x18\x02 \x01(\x0e\x32!.jina.ControlRequestProto.Command\x12,\n\x0frelatedEntities\x18\x03 \x03(\x0b\x32\x13.jina.RelatedEntity\"3\n\x07\x43ommand\x12\n\n\x06STATUS\x10\x00\x12\x0c\n\x08\x41\x43TIVATE\x10\x01\x12\x0e\n\nDEACTIVATE\x10\x02\"\xa5\x02\n\x10\x44\x61taRequestProto\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.jina.HeaderProto\x12+\n\nparameters\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12 \n\x06routes\x18\x03 \x03(\x0b\x32\x10.jina.RouteProto\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.jina.DataRequestProto.DataContentProto\x1ah\n\x10\x44\x61taContentProto\x12%\n\x04\x64ocs\x18\x01 \x03(\x0b\x32\x17.docarray.DocumentProto\x12-\n\x0cgroundtruths\x18\x02 \x03(\x0b\x32\x17.docarray.DocumentProto\"@\n\x14\x44\x61taRequestListProto\x12(\n\x08requests\x18\x01 \x03(\x0b\x32\x16.jina.DataRequestProto2b\n\x15JinaControlRequestRPC\x12I\n\x0fprocess_control\x12\x19.jina.ControlRequestProto\x1a\x19.jina.ControlRequestProto\"\x00\x32Z\n\x12JinaDataRequestRPC\x12\x44\n\x0cprocess_data\x12\x1a.jina.DataRequestListProto\x1a\x16.jina.DataRequestProto\"\x00\x32\x63\n\x18JinaSingleDataRequestRPC\x12G\n\x13process_single_data\x12\x16.jina.DataRequestProto\x1a\x16.jina.DataRequestProto\"\x00\x32G\n\x07JinaRPC\x12<\n\x04\x43\x61ll\x12\x16.jina.DataRequestProto\x1a\x16.jina.DataRequestProto\"\x00(\x01\x30\x01\x62\x06proto3')



_ROUTEPROTO = DESCRIPTOR.message_types_by_name['RouteProto']
_HEADERPROTO = DESCRIPTOR.message_types_by_name['HeaderProto']
_STATUSPROTO = DESCRIPTOR.message_types_by_name['StatusProto']
_STATUSPROTO_EXCEPTIONPROTO = _STATUSPROTO.nested_types_by_name['ExceptionProto']
_RELATEDENTITY = DESCRIPTOR.message_types_by_name['RelatedEntity']
_CONTROLREQUESTPROTO = DESCRIPTOR.message_types_by_name['ControlRequestProto']
_DATAREQUESTPROTO = DESCRIPTOR.message_types_by_name['DataRequestProto']
_DATAREQUESTPROTO_DATACONTENTPROTO = _DATAREQUESTPROTO.nested_types_by_name['DataContentProto']
_DATAREQUESTLISTPROTO = DESCRIPTOR.message_types_by_name['DataRequestListProto']
_STATUSPROTO_STATUSCODE = _STATUSPROTO.enum_types_by_name['StatusCode']
_CONTROLREQUESTPROTO_COMMAND = _CONTROLREQUESTPROTO.enum_types_by_name['Command']
RouteProto = _reflection.GeneratedProtocolMessageType('RouteProto', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.RouteProto)
  })
_sym_db.RegisterMessage(RouteProto)

HeaderProto = _reflection.GeneratedProtocolMessageType('HeaderProto', (_message.Message,), {
  'DESCRIPTOR' : _HEADERPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.HeaderProto)
  })
_sym_db.RegisterMessage(HeaderProto)

StatusProto = _reflection.GeneratedProtocolMessageType('StatusProto', (_message.Message,), {

  'ExceptionProto' : _reflection.GeneratedProtocolMessageType('ExceptionProto', (_message.Message,), {
    'DESCRIPTOR' : _STATUSPROTO_EXCEPTIONPROTO,
    '__module__' : 'jina_pb2'
    # @@protoc_insertion_point(class_scope:jina.StatusProto.ExceptionProto)
    })
  ,
  'DESCRIPTOR' : _STATUSPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.StatusProto)
  })
_sym_db.RegisterMessage(StatusProto)
_sym_db.RegisterMessage(StatusProto.ExceptionProto)

RelatedEntity = _reflection.GeneratedProtocolMessageType('RelatedEntity', (_message.Message,), {
  'DESCRIPTOR' : _RELATEDENTITY,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.RelatedEntity)
  })
_sym_db.RegisterMessage(RelatedEntity)

ControlRequestProto = _reflection.GeneratedProtocolMessageType('ControlRequestProto', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLREQUESTPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.ControlRequestProto)
  })
_sym_db.RegisterMessage(ControlRequestProto)

DataRequestProto = _reflection.GeneratedProtocolMessageType('DataRequestProto', (_message.Message,), {

  'DataContentProto' : _reflection.GeneratedProtocolMessageType('DataContentProto', (_message.Message,), {
    'DESCRIPTOR' : _DATAREQUESTPROTO_DATACONTENTPROTO,
    '__module__' : 'jina_pb2'
    # @@protoc_insertion_point(class_scope:jina.DataRequestProto.DataContentProto)
    })
  ,
  'DESCRIPTOR' : _DATAREQUESTPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.DataRequestProto)
  })
_sym_db.RegisterMessage(DataRequestProto)
_sym_db.RegisterMessage(DataRequestProto.DataContentProto)

DataRequestListProto = _reflection.GeneratedProtocolMessageType('DataRequestListProto', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQUESTLISTPROTO,
  '__module__' : 'jina_pb2'
  # @@protoc_insertion_point(class_scope:jina.DataRequestListProto)
  })
_sym_db.RegisterMessage(DataRequestListProto)

_JINACONTROLREQUESTRPC = DESCRIPTOR.services_by_name['JinaControlRequestRPC']
_JINADATAREQUESTRPC = DESCRIPTOR.services_by_name['JinaDataRequestRPC']
_JINASINGLEDATAREQUESTRPC = DESCRIPTOR.services_by_name['JinaSingleDataRequestRPC']
_JINARPC = DESCRIPTOR.services_by_name['JinaRPC']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROUTEPROTO._serialized_start=100
  _ROUTEPROTO._serialized_end=254
  _HEADERPROTO._serialized_start=257
  _HEADERPROTO._serialized_end=451
  _STATUSPROTO._serialized_start=454
  _STATUSPROTO._serialized_end=789
  _STATUSPROTO_EXCEPTIONPROTO._serialized_start=587
  _STATUSPROTO_EXCEPTIONPROTO._serialized_end=665
  _STATUSPROTO_STATUSCODE._serialized_start=667
  _STATUSPROTO_STATUSCODE._serialized_end=789
  _RELATEDENTITY._serialized_start=791
  _RELATEDENTITY._serialized_end=885
  _CONTROLREQUESTPROTO._serialized_start=888
  _CONTROLREQUESTPROTO._serialized_end=1095
  _CONTROLREQUESTPROTO_COMMAND._serialized_start=1044
  _CONTROLREQUESTPROTO_COMMAND._serialized_end=1095
  _DATAREQUESTPROTO._serialized_start=1098
  _DATAREQUESTPROTO._serialized_end=1391
  _DATAREQUESTPROTO_DATACONTENTPROTO._serialized_start=1287
  _DATAREQUESTPROTO_DATACONTENTPROTO._serialized_end=1391
  _DATAREQUESTLISTPROTO._serialized_start=1393
  _DATAREQUESTLISTPROTO._serialized_end=1457
  _JINACONTROLREQUESTRPC._serialized_start=1459
  _JINACONTROLREQUESTRPC._serialized_end=1557
  _JINADATAREQUESTRPC._serialized_start=1559
  _JINADATAREQUESTRPC._serialized_end=1649
  _JINASINGLEDATAREQUESTRPC._serialized_start=1651
  _JINASINGLEDATAREQUESTRPC._serialized_end=1750
  _JINARPC._serialized_start=1752
  _JINARPC._serialized_end=1823
# @@protoc_insertion_point(module_scope)
