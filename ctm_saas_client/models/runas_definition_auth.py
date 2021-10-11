# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.30
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ctm_saas_client.configuration import Configuration


class RunasDefinitionAuth(object):
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
        'controlm_server': 'str',
        'privilege': 'str'
    }

    attribute_map = {
        'controlm_server': 'ControlmServer',
        'privilege': 'Privilege'
    }

    def __init__(self, controlm_server=None, privilege=None, _configuration=None):  # noqa: E501
        """RunasDefinitionAuth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._controlm_server = None
        self._privilege = None
        self.discriminator = None

        if controlm_server is not None:
            self.controlm_server = controlm_server
        if privilege is not None:
            self.privilege = privilege

    @property
    def controlm_server(self):
        """Gets the controlm_server of this RunasDefinitionAuth.  # noqa: E501

        control-M server name  # noqa: E501

        :return: The controlm_server of this RunasDefinitionAuth.  # noqa: E501
        :rtype: str
        """
        return self._controlm_server

    @controlm_server.setter
    def controlm_server(self, controlm_server):
        """Sets the controlm_server of this RunasDefinitionAuth.

        control-M server name  # noqa: E501

        :param controlm_server: The controlm_server of this RunasDefinitionAuth.  # noqa: E501
        :type: str
        """

        self._controlm_server = controlm_server

    @property
    def privilege(self):
        """Gets the privilege of this RunasDefinitionAuth.  # noqa: E501

        access level (full, update, browse)  # noqa: E501

        :return: The privilege of this RunasDefinitionAuth.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this RunasDefinitionAuth.

        access level (full, update, browse)  # noqa: E501

        :param privilege: The privilege of this RunasDefinitionAuth.  # noqa: E501
        :type: str
        """

        self._privilege = privilege

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
        if issubclass(RunasDefinitionAuth, dict):
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
        if not isinstance(other, RunasDefinitionAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunasDefinitionAuth):
            return True

        return self.to_dict() != other.to_dict()
