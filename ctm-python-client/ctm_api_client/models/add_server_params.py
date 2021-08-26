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


class AddServerParams(object):
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
        'host': 'str',
        'ctm': 'str',
        'id': 'str',
        'port': 'int'
    }

    attribute_map = {
        'host': 'host',
        'ctm': 'ctm',
        'id': 'id',
        'port': 'port'
    }

    def __init__(self, host=None, ctm=None, id=None, port=None, _configuration=None):  # noqa: E501
        """AddServerParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host = None
        self._ctm = None
        self._id = None
        self._port = None
        self.discriminator = None

        self.host = host
        self.ctm = ctm
        self.id = id
        if port is not None:
            self.port = port

    @property
    def host(self):
        """Gets the host of this AddServerParams.  # noqa: E501

        The Control-M Server host name.  # noqa: E501

        :return: The host of this AddServerParams.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AddServerParams.

        The Control-M Server host name.  # noqa: E501

        :param host: The host of this AddServerParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def ctm(self):
        """Gets the ctm of this AddServerParams.  # noqa: E501

        The Control-M Server name.  # noqa: E501

        :return: The ctm of this AddServerParams.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this AddServerParams.

        The Control-M Server name.  # noqa: E501

        :param ctm: The ctm of this AddServerParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ctm is None:
            raise ValueError("Invalid value for `ctm`, must not be `None`")  # noqa: E501

        self._ctm = ctm

    @property
    def id(self):
        """Gets the id of this AddServerParams.  # noqa: E501

        The id of the Control-M Server, 3 digits id  # noqa: E501

        :return: The id of this AddServerParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddServerParams.

        The id of the Control-M Server, 3 digits id  # noqa: E501

        :param id: The id of this AddServerParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def port(self):
        """Gets the port of this AddServerParams.  # noqa: E501

        The Control-M Server port number.  # noqa: E501

        :return: The port of this AddServerParams.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AddServerParams.

        The Control-M Server port number.  # noqa: E501

        :param port: The port of this AddServerParams.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if issubclass(AddServerParams, dict):
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
        if not isinstance(other, AddServerParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddServerParams):
            return True

        return self.to_dict() != other.to_dict()
