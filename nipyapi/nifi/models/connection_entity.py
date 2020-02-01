# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.11.1-SNAPSHOT
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConnectionEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'revision': 'RevisionDTO',
        'id': 'str',
        'uri': 'str',
        'position': 'PositionDTO',
        'permissions': 'PermissionsDTO',
        'bulletins': 'list[BulletinEntity]',
        'disconnected_node_acknowledged': 'bool',
        'component': 'ConnectionDTO',
        'status': 'ConnectionStatusDTO',
        'bends': 'list[PositionDTO]',
        'label_index': 'int',
        'getz_index': 'int',
        'source_id': 'str',
        'source_group_id': 'str',
        'source_type': 'str',
        'destination_id': 'str',
        'destination_group_id': 'str',
        'destination_type': 'str'
    }

    attribute_map = {
        'revision': 'revision',
        'id': 'id',
        'uri': 'uri',
        'position': 'position',
        'permissions': 'permissions',
        'bulletins': 'bulletins',
        'disconnected_node_acknowledged': 'disconnectedNodeAcknowledged',
        'component': 'component',
        'status': 'status',
        'bends': 'bends',
        'label_index': 'labelIndex',
        'getz_index': 'getzIndex',
        'source_id': 'sourceId',
        'source_group_id': 'sourceGroupId',
        'source_type': 'sourceType',
        'destination_id': 'destinationId',
        'destination_group_id': 'destinationGroupId',
        'destination_type': 'destinationType'
    }

    def __init__(self, revision=None, id=None, uri=None, position=None, permissions=None, bulletins=None, disconnected_node_acknowledged=None, component=None, status=None, bends=None, label_index=None, getz_index=None, source_id=None, source_group_id=None, source_type=None, destination_id=None, destination_group_id=None, destination_type=None):
        """
        ConnectionEntity - a model defined in Swagger
        """

        self._revision = None
        self._id = None
        self._uri = None
        self._position = None
        self._permissions = None
        self._bulletins = None
        self._disconnected_node_acknowledged = None
        self._component = None
        self._status = None
        self._bends = None
        self._label_index = None
        self._getz_index = None
        self._source_id = None
        self._source_group_id = None
        self._source_type = None
        self._destination_id = None
        self._destination_group_id = None
        self._destination_type = None

        if revision is not None:
          self.revision = revision
        if id is not None:
          self.id = id
        if uri is not None:
          self.uri = uri
        if position is not None:
          self.position = position
        if permissions is not None:
          self.permissions = permissions
        if bulletins is not None:
          self.bulletins = bulletins
        if disconnected_node_acknowledged is not None:
          self.disconnected_node_acknowledged = disconnected_node_acknowledged
        if component is not None:
          self.component = component
        if status is not None:
          self.status = status
        if bends is not None:
          self.bends = bends
        if label_index is not None:
          self.label_index = label_index
        if getz_index is not None:
          self.getz_index = getz_index
        if source_id is not None:
          self.source_id = source_id
        if source_group_id is not None:
          self.source_group_id = source_group_id
        self.source_type = source_type
        if destination_id is not None:
          self.destination_id = destination_id
        if destination_group_id is not None:
          self.destination_group_id = destination_group_id
        self.destination_type = destination_type

    @property
    def revision(self):
        """
        Gets the revision of this ConnectionEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :return: The revision of this ConnectionEntity.
        :rtype: RevisionDTO
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ConnectionEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :param revision: The revision of this ConnectionEntity.
        :type: RevisionDTO
        """

        self._revision = revision

    @property
    def id(self):
        """
        Gets the id of this ConnectionEntity.
        The id of the component.

        :return: The id of this ConnectionEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionEntity.
        The id of the component.

        :param id: The id of this ConnectionEntity.
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """
        Gets the uri of this ConnectionEntity.
        The URI for futures requests to the component.

        :return: The uri of this ConnectionEntity.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ConnectionEntity.
        The URI for futures requests to the component.

        :param uri: The uri of this ConnectionEntity.
        :type: str
        """

        self._uri = uri

    @property
    def position(self):
        """
        Gets the position of this ConnectionEntity.
        The position of this component in the UI if applicable.

        :return: The position of this ConnectionEntity.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ConnectionEntity.
        The position of this component in the UI if applicable.

        :param position: The position of this ConnectionEntity.
        :type: PositionDTO
        """

        self._position = position

    @property
    def permissions(self):
        """
        Gets the permissions of this ConnectionEntity.
        The permissions for this component.

        :return: The permissions of this ConnectionEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this ConnectionEntity.
        The permissions for this component.

        :param permissions: The permissions of this ConnectionEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def bulletins(self):
        """
        Gets the bulletins of this ConnectionEntity.
        The bulletins for this component.

        :return: The bulletins of this ConnectionEntity.
        :rtype: list[BulletinEntity]
        """
        return self._bulletins

    @bulletins.setter
    def bulletins(self, bulletins):
        """
        Sets the bulletins of this ConnectionEntity.
        The bulletins for this component.

        :param bulletins: The bulletins of this ConnectionEntity.
        :type: list[BulletinEntity]
        """

        self._bulletins = bulletins

    @property
    def disconnected_node_acknowledged(self):
        """
        Gets the disconnected_node_acknowledged of this ConnectionEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :return: The disconnected_node_acknowledged of this ConnectionEntity.
        :rtype: bool
        """
        return self._disconnected_node_acknowledged

    @disconnected_node_acknowledged.setter
    def disconnected_node_acknowledged(self, disconnected_node_acknowledged):
        """
        Sets the disconnected_node_acknowledged of this ConnectionEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :param disconnected_node_acknowledged: The disconnected_node_acknowledged of this ConnectionEntity.
        :type: bool
        """

        self._disconnected_node_acknowledged = disconnected_node_acknowledged

    @property
    def component(self):
        """
        Gets the component of this ConnectionEntity.

        :return: The component of this ConnectionEntity.
        :rtype: ConnectionDTO
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this ConnectionEntity.

        :param component: The component of this ConnectionEntity.
        :type: ConnectionDTO
        """

        self._component = component

    @property
    def status(self):
        """
        Gets the status of this ConnectionEntity.
        The status of the connection.

        :return: The status of this ConnectionEntity.
        :rtype: ConnectionStatusDTO
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConnectionEntity.
        The status of the connection.

        :param status: The status of this ConnectionEntity.
        :type: ConnectionStatusDTO
        """

        self._status = status

    @property
    def bends(self):
        """
        Gets the bends of this ConnectionEntity.
        The bend points on the connection.

        :return: The bends of this ConnectionEntity.
        :rtype: list[PositionDTO]
        """
        return self._bends

    @bends.setter
    def bends(self, bends):
        """
        Sets the bends of this ConnectionEntity.
        The bend points on the connection.

        :param bends: The bends of this ConnectionEntity.
        :type: list[PositionDTO]
        """

        self._bends = bends

    @property
    def label_index(self):
        """
        Gets the label_index of this ConnectionEntity.
        The index of the bend point where to place the connection label.

        :return: The label_index of this ConnectionEntity.
        :rtype: int
        """
        return self._label_index

    @label_index.setter
    def label_index(self, label_index):
        """
        Sets the label_index of this ConnectionEntity.
        The index of the bend point where to place the connection label.

        :param label_index: The label_index of this ConnectionEntity.
        :type: int
        """

        self._label_index = label_index

    @property
    def getz_index(self):
        """
        Gets the getz_index of this ConnectionEntity.
        The z index of the connection.

        :return: The getz_index of this ConnectionEntity.
        :rtype: int
        """
        return self._getz_index

    @getz_index.setter
    def getz_index(self, getz_index):
        """
        Sets the getz_index of this ConnectionEntity.
        The z index of the connection.

        :param getz_index: The getz_index of this ConnectionEntity.
        :type: int
        """

        self._getz_index = getz_index

    @property
    def source_id(self):
        """
        Gets the source_id of this ConnectionEntity.
        The identifier of the source of this connection.

        :return: The source_id of this ConnectionEntity.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this ConnectionEntity.
        The identifier of the source of this connection.

        :param source_id: The source_id of this ConnectionEntity.
        :type: str
        """

        self._source_id = source_id

    @property
    def source_group_id(self):
        """
        Gets the source_group_id of this ConnectionEntity.
        The identifier of the group of the source of this connection.

        :return: The source_group_id of this ConnectionEntity.
        :rtype: str
        """
        return self._source_group_id

    @source_group_id.setter
    def source_group_id(self, source_group_id):
        """
        Sets the source_group_id of this ConnectionEntity.
        The identifier of the group of the source of this connection.

        :param source_group_id: The source_group_id of this ConnectionEntity.
        :type: str
        """

        self._source_group_id = source_group_id

    @property
    def source_type(self):
        """
        Gets the source_type of this ConnectionEntity.
        The type of component the source connectable is.

        :return: The source_type of this ConnectionEntity.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this ConnectionEntity.
        The type of component the source connectable is.

        :param source_type: The source_type of this ConnectionEntity.
        :type: str
        """
        if source_type is None:
            raise ValueError("Invalid value for `source_type`, must not be `None`")
        allowed_values = ["PROCESSOR", "REMOTE_INPUT_PORT", "REMOTE_OUTPUT_PORT", "INPUT_PORT", "OUTPUT_PORT", "FUNNEL"]
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def destination_id(self):
        """
        Gets the destination_id of this ConnectionEntity.
        The identifier of the destination of this connection.

        :return: The destination_id of this ConnectionEntity.
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """
        Sets the destination_id of this ConnectionEntity.
        The identifier of the destination of this connection.

        :param destination_id: The destination_id of this ConnectionEntity.
        :type: str
        """

        self._destination_id = destination_id

    @property
    def destination_group_id(self):
        """
        Gets the destination_group_id of this ConnectionEntity.
        The identifier of the group of the destination of this connection.

        :return: The destination_group_id of this ConnectionEntity.
        :rtype: str
        """
        return self._destination_group_id

    @destination_group_id.setter
    def destination_group_id(self, destination_group_id):
        """
        Sets the destination_group_id of this ConnectionEntity.
        The identifier of the group of the destination of this connection.

        :param destination_group_id: The destination_group_id of this ConnectionEntity.
        :type: str
        """

        self._destination_group_id = destination_group_id

    @property
    def destination_type(self):
        """
        Gets the destination_type of this ConnectionEntity.
        The type of component the destination connectable is.

        :return: The destination_type of this ConnectionEntity.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this ConnectionEntity.
        The type of component the destination connectable is.

        :param destination_type: The destination_type of this ConnectionEntity.
        :type: str
        """
        if destination_type is None:
            raise ValueError("Invalid value for `destination_type`, must not be `None`")
        allowed_values = ["PROCESSOR", "REMOTE_INPUT_PORT", "REMOTE_OUTPUT_PORT", "INPUT_PORT", "OUTPUT_PORT", "FUNNEL"]
        if destination_type not in allowed_values:
            raise ValueError(
                "Invalid value for `destination_type` ({0}), must be one of {1}"
                .format(destination_type, allowed_values)
            )

        self._destination_type = destination_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ConnectionEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
