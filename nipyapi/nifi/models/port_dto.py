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


class PortDTO(object):
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
        'id': 'str',
        'versioned_component_id': 'str',
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'name': 'str',
        'comments': 'str',
        'state': 'str',
        'type': 'str',
        'transmitting': 'bool',
        'concurrently_schedulable_task_count': 'int',
        'user_access_control': 'list[str]',
        'group_access_control': 'list[str]',
        'allow_remote_access': 'bool',
        'validation_errors': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'name': 'name',
        'comments': 'comments',
        'state': 'state',
        'type': 'type',
        'transmitting': 'transmitting',
        'concurrently_schedulable_task_count': 'concurrentlySchedulableTaskCount',
        'user_access_control': 'userAccessControl',
        'group_access_control': 'groupAccessControl',
        'allow_remote_access': 'allowRemoteAccess',
        'validation_errors': 'validationErrors'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, name=None, comments=None, state=None, type=None, transmitting=None, concurrently_schedulable_task_count=None, user_access_control=None, group_access_control=None, allow_remote_access=None, validation_errors=None):
        """
        PortDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._name = None
        self._comments = None
        self._state = None
        self._type = None
        self._transmitting = None
        self._concurrently_schedulable_task_count = None
        self._user_access_control = None
        self._group_access_control = None
        self._allow_remote_access = None
        self._validation_errors = None

        if id is not None:
          self.id = id
        if versioned_component_id is not None:
          self.versioned_component_id = versioned_component_id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if name is not None:
          self.name = name
        if comments is not None:
          self.comments = comments
        if state is not None:
          self.state = state
        if type is not None:
          self.type = type
        if transmitting is not None:
          self.transmitting = transmitting
        if concurrently_schedulable_task_count is not None:
          self.concurrently_schedulable_task_count = concurrently_schedulable_task_count
        if user_access_control is not None:
          self.user_access_control = user_access_control
        if group_access_control is not None:
          self.group_access_control = group_access_control
        if allow_remote_access is not None:
          self.allow_remote_access = allow_remote_access
        if validation_errors is not None:
          self.validation_errors = validation_errors

    @property
    def id(self):
        """
        Gets the id of this PortDTO.
        The id of the component.

        :return: The id of this PortDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PortDTO.
        The id of the component.

        :param id: The id of this PortDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this PortDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this PortDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this PortDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this PortDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this PortDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this PortDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this PortDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this PortDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this PortDTO.
        The position of this component in the UI if applicable.

        :return: The position of this PortDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this PortDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this PortDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def name(self):
        """
        Gets the name of this PortDTO.
        The name of the port.

        :return: The name of this PortDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PortDTO.
        The name of the port.

        :param name: The name of this PortDTO.
        :type: str
        """

        self._name = name

    @property
    def comments(self):
        """
        Gets the comments of this PortDTO.
        The comments for the port.

        :return: The comments of this PortDTO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this PortDTO.
        The comments for the port.

        :param comments: The comments of this PortDTO.
        :type: str
        """

        self._comments = comments

    @property
    def state(self):
        """
        Gets the state of this PortDTO.
        The state of the port.

        :return: The state of this PortDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PortDTO.
        The state of the port.

        :param state: The state of this PortDTO.
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED", "DISABLED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def type(self):
        """
        Gets the type of this PortDTO.
        The type of port.

        :return: The type of this PortDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PortDTO.
        The type of port.

        :param type: The type of this PortDTO.
        :type: str
        """
        allowed_values = ["INPUT_PORT", "OUTPUT_PORT"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def transmitting(self):
        """
        Gets the transmitting of this PortDTO.
        Whether the port has incoming or output connections to a remote NiFi. This is only applicable when the port is allowed to be accessed remotely.

        :return: The transmitting of this PortDTO.
        :rtype: bool
        """
        return self._transmitting

    @transmitting.setter
    def transmitting(self, transmitting):
        """
        Sets the transmitting of this PortDTO.
        Whether the port has incoming or output connections to a remote NiFi. This is only applicable when the port is allowed to be accessed remotely.

        :param transmitting: The transmitting of this PortDTO.
        :type: bool
        """

        self._transmitting = transmitting

    @property
    def concurrently_schedulable_task_count(self):
        """
        Gets the concurrently_schedulable_task_count of this PortDTO.
        The number of tasks that should be concurrently scheduled for the port.

        :return: The concurrently_schedulable_task_count of this PortDTO.
        :rtype: int
        """
        return self._concurrently_schedulable_task_count

    @concurrently_schedulable_task_count.setter
    def concurrently_schedulable_task_count(self, concurrently_schedulable_task_count):
        """
        Sets the concurrently_schedulable_task_count of this PortDTO.
        The number of tasks that should be concurrently scheduled for the port.

        :param concurrently_schedulable_task_count: The concurrently_schedulable_task_count of this PortDTO.
        :type: int
        """

        self._concurrently_schedulable_task_count = concurrently_schedulable_task_count

    @property
    def user_access_control(self):
        """
        Gets the user_access_control of this PortDTO.
        The users that are allowed to access the port.

        :return: The user_access_control of this PortDTO.
        :rtype: list[str]
        """
        return self._user_access_control

    @user_access_control.setter
    def user_access_control(self, user_access_control):
        """
        Sets the user_access_control of this PortDTO.
        The users that are allowed to access the port.

        :param user_access_control: The user_access_control of this PortDTO.
        :type: list[str]
        """

        self._user_access_control = user_access_control

    @property
    def group_access_control(self):
        """
        Gets the group_access_control of this PortDTO.
        The user groups that are allowed to access the port.

        :return: The group_access_control of this PortDTO.
        :rtype: list[str]
        """
        return self._group_access_control

    @group_access_control.setter
    def group_access_control(self, group_access_control):
        """
        Sets the group_access_control of this PortDTO.
        The user groups that are allowed to access the port.

        :param group_access_control: The group_access_control of this PortDTO.
        :type: list[str]
        """

        self._group_access_control = group_access_control

    @property
    def allow_remote_access(self):
        """
        Gets the allow_remote_access of this PortDTO.
        Whether this port can be accessed remotely via Site-to-Site protocol.

        :return: The allow_remote_access of this PortDTO.
        :rtype: bool
        """
        return self._allow_remote_access

    @allow_remote_access.setter
    def allow_remote_access(self, allow_remote_access):
        """
        Sets the allow_remote_access of this PortDTO.
        Whether this port can be accessed remotely via Site-to-Site protocol.

        :param allow_remote_access: The allow_remote_access of this PortDTO.
        :type: bool
        """

        self._allow_remote_access = allow_remote_access

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this PortDTO.
        Gets the validation errors from this port. These validation errors represent the problems with the port that must be resolved before it can be started.

        :return: The validation_errors of this PortDTO.
        :rtype: list[str]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this PortDTO.
        Gets the validation errors from this port. These validation errors represent the problems with the port that must be resolved before it can be started.

        :param validation_errors: The validation_errors of this PortDTO.
        :type: list[str]
        """

        self._validation_errors = validation_errors

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
        if not isinstance(other, PortDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
