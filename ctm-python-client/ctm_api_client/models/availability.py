# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.215
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ctm-python-client.ctm_api_client.configuration import Configuration


class Availability(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'type': 'str',
        'name': 'str',
        'status': 'str',
        'message': 'str',
        'key': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'status': 'status',
        'message': 'message',
        'key': 'key'
    }

    def __init__(self, type=None, name=None, status=None, message=None, key=None, _configuration=None):  # noqa: E501
        """Availability - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._name = None
        self._status = None
        self._message = None
        self._key = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if key is not None:
            self.key = key

    @property
    def type(self):
        """Gets the type of this Availability.  # noqa: E501

        the type of the availability stat  # noqa: E501

        :return: The type of this Availability.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Availability.

        the type of the availability stat  # noqa: E501

        :param type: The type of this Availability.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this Availability.  # noqa: E501

        the name of the stat  # noqa: E501

        :return: The name of this Availability.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Availability.

        the name of the stat  # noqa: E501

        :param name: The name of this Availability.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Availability.  # noqa: E501

        the current status  # noqa: E501

        :return: The status of this Availability.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Availability.

        the current status  # noqa: E501

        :param status: The status of this Availability.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this Availability.  # noqa: E501

        A message representing the problem  # noqa: E501

        :return: The message of this Availability.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Availability.

        A message representing the problem  # noqa: E501

        :param message: The message of this Availability.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def key(self):
        """Gets the key of this Availability.  # noqa: E501

        A unique key for the metric  # noqa: E501

        :return: The key of this Availability.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Availability.

        A unique key for the metric  # noqa: E501

        :param key: The key of this Availability.  # noqa: E501
        :type: str
        """

        self._key = key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Availability, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Availability):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Availability):
            return True

        return self.to_dict() != other.to_dict()
