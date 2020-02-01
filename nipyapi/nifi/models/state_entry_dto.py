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


class StateEntryDTO(object):
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
        'key': 'str',
        'value': 'str',
        'cluster_node_id': 'str',
        'cluster_node_address': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'cluster_node_id': 'clusterNodeId',
        'cluster_node_address': 'clusterNodeAddress'
    }

    def __init__(self, key=None, value=None, cluster_node_id=None, cluster_node_address=None):
        """
        StateEntryDTO - a model defined in Swagger
        """

        self._key = None
        self._value = None
        self._cluster_node_id = None
        self._cluster_node_address = None

        if key is not None:
          self.key = key
        if value is not None:
          self.value = value
        if cluster_node_id is not None:
          self.cluster_node_id = cluster_node_id
        if cluster_node_address is not None:
          self.cluster_node_address = cluster_node_address

    @property
    def key(self):
        """
        Gets the key of this StateEntryDTO.
        The key for this state.

        :return: The key of this StateEntryDTO.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this StateEntryDTO.
        The key for this state.

        :param key: The key of this StateEntryDTO.
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """
        Gets the value of this StateEntryDTO.
        The value for this state.

        :return: The value of this StateEntryDTO.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this StateEntryDTO.
        The value for this state.

        :param value: The value of this StateEntryDTO.
        :type: str
        """

        self._value = value

    @property
    def cluster_node_id(self):
        """
        Gets the cluster_node_id of this StateEntryDTO.
        The identifier for the node where the state originated.

        :return: The cluster_node_id of this StateEntryDTO.
        :rtype: str
        """
        return self._cluster_node_id

    @cluster_node_id.setter
    def cluster_node_id(self, cluster_node_id):
        """
        Sets the cluster_node_id of this StateEntryDTO.
        The identifier for the node where the state originated.

        :param cluster_node_id: The cluster_node_id of this StateEntryDTO.
        :type: str
        """

        self._cluster_node_id = cluster_node_id

    @property
    def cluster_node_address(self):
        """
        Gets the cluster_node_address of this StateEntryDTO.
        The label for the node where the state originated.

        :return: The cluster_node_address of this StateEntryDTO.
        :rtype: str
        """
        return self._cluster_node_address

    @cluster_node_address.setter
    def cluster_node_address(self, cluster_node_address):
        """
        Sets the cluster_node_address of this StateEntryDTO.
        The label for the node where the state originated.

        :param cluster_node_address: The cluster_node_address of this StateEntryDTO.
        :type: str
        """

        self._cluster_node_address = cluster_node_address

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
        if not isinstance(other, StateEntryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
