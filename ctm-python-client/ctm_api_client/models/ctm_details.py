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


class CtmDetails(object):
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
        'name': 'str',
        'host': 'str',
        'state': 'str',
        'message': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'host': 'host',
        'state': 'state',
        'message': 'message',
        'version': 'version'
    }

    def __init__(self, name=None, host=None, state=None, message=None, version=None, _configuration=None):  # noqa: E501
        """CtmDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._host = None
        self._state = None
        self._message = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if state is not None:
            self.state = state
        if message is not None:
            self.message = message
        if version is not None:
            self.version = version

    @property
    def name(self):
        """Gets the name of this CtmDetails.  # noqa: E501

        The unique name of the Control-M Server.  # noqa: E501

        :return: The name of this CtmDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CtmDetails.

        The unique name of the Control-M Server.  # noqa: E501

        :param name: The name of this CtmDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """Gets the host of this CtmDetails.  # noqa: E501

        The hostname of the Control-M Server is running on.  # noqa: E501

        :return: The host of this CtmDetails.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CtmDetails.

        The hostname of the Control-M Server is running on.  # noqa: E501

        :param host: The host of this CtmDetails.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def state(self):
        """Gets the state of this CtmDetails.  # noqa: E501

        Control-M Server state [up|down].  # noqa: E501

        :return: The state of this CtmDetails.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CtmDetails.

        Control-M Server state [up|down].  # noqa: E501

        :param state: The state of this CtmDetails.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def message(self):
        """Gets the message of this CtmDetails.  # noqa: E501

        Control-M Server message describing the communication status.  # noqa: E501

        :return: The message of this CtmDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CtmDetails.

        Control-M Server message describing the communication status.  # noqa: E501

        :param message: The message of this CtmDetails.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def version(self):
        """Gets the version of this CtmDetails.  # noqa: E501

        Control-M Server version.  # noqa: E501

        :return: The version of this CtmDetails.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CtmDetails.

        Control-M Server version.  # noqa: E501

        :param version: The version of this CtmDetails.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(CtmDetails, dict):
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
        if not isinstance(other, CtmDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CtmDetails):
            return True

        return self.to_dict() != other.to_dict()
