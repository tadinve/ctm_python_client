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


class SshKeyProperties(object):
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
        'key_name': 'str',
        'key_passphrase': 'str',
        'key_size': 'int'
    }

    attribute_map = {
        'key_name': 'keyName',
        'key_passphrase': 'keyPassphrase',
        'key_size': 'keySize'
    }

    def __init__(self, key_name=None, key_passphrase=None, key_size=2048, _configuration=None):  # noqa: E501
        """SshKeyProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key_name = None
        self._key_passphrase = None
        self._key_size = None
        self.discriminator = None

        if key_name is not None:
            self.key_name = key_name
        if key_passphrase is not None:
            self.key_passphrase = key_passphrase
        if key_size is not None:
            self.key_size = key_size

    @property
    def key_name(self):
        """Gets the key_name of this SshKeyProperties.  # noqa: E501

        External user data REQUIRED  # noqa: E501

        :return: The key_name of this SshKeyProperties.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this SshKeyProperties.

        External user data REQUIRED  # noqa: E501

        :param key_name: The key_name of this SshKeyProperties.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def key_passphrase(self):
        """Gets the key_passphrase of this SshKeyProperties.  # noqa: E501

        SSH Key passphrase REQUIRED  # noqa: E501

        :return: The key_passphrase of this SshKeyProperties.  # noqa: E501
        :rtype: str
        """
        return self._key_passphrase

    @key_passphrase.setter
    def key_passphrase(self, key_passphrase):
        """Sets the key_passphrase of this SshKeyProperties.

        SSH Key passphrase REQUIRED  # noqa: E501

        :param key_passphrase: The key_passphrase of this SshKeyProperties.  # noqa: E501
        :type: str
        """

        self._key_passphrase = key_passphrase

    @property
    def key_size(self):
        """Gets the key_size of this SshKeyProperties.  # noqa: E501

        SSH Key size (default 2048)  # noqa: E501

        :return: The key_size of this SshKeyProperties.  # noqa: E501
        :rtype: int
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """Sets the key_size of this SshKeyProperties.

        SSH Key size (default 2048)  # noqa: E501

        :param key_size: The key_size of this SshKeyProperties.  # noqa: E501
        :type: int
        """

        self._key_size = key_size

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
        if issubclass(SshKeyProperties, dict):
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
        if not isinstance(other, SshKeyProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SshKeyProperties):
            return True

        return self.to_dict() != other.to_dict()
