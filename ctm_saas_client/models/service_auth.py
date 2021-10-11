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


class ServiceAuth(object):
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
        'privilege': 'str',
        'name': 'str',
        'allowed_actions': 'ServiceAuthAction'
    }

    attribute_map = {
        'privilege': 'Privilege',
        'name': 'Name',
        'allowed_actions': 'AllowedActions'
    }

    def __init__(self, privilege=None, name=None, allowed_actions=None, _configuration=None):  # noqa: E501
        """ServiceAuth - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._privilege = None
        self._name = None
        self._allowed_actions = None
        self.discriminator = None

        if privilege is not None:
            self.privilege = privilege
        if name is not None:
            self.name = name
        if allowed_actions is not None:
            self.allowed_actions = allowed_actions

    @property
    def privilege(self):
        """Gets the privilege of this ServiceAuth.  # noqa: E501

        access level (Full, Update, Browse, None)  # noqa: E501

        :return: The privilege of this ServiceAuth.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this ServiceAuth.

        access level (Full, Update, Browse, None)  # noqa: E501

        :param privilege: The privilege of this ServiceAuth.  # noqa: E501
        :type: str
        """

        self._privilege = privilege

    @property
    def name(self):
        """Gets the name of this ServiceAuth.  # noqa: E501

        service name  # noqa: E501

        :return: The name of this ServiceAuth.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceAuth.

        service name  # noqa: E501

        :param name: The name of this ServiceAuth.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def allowed_actions(self):
        """Gets the allowed_actions of this ServiceAuth.  # noqa: E501

        active list  # noqa: E501

        :return: The allowed_actions of this ServiceAuth.  # noqa: E501
        :rtype: ServiceAuthAction
        """
        return self._allowed_actions

    @allowed_actions.setter
    def allowed_actions(self, allowed_actions):
        """Sets the allowed_actions of this ServiceAuth.

        active list  # noqa: E501

        :param allowed_actions: The allowed_actions of this ServiceAuth.  # noqa: E501
        :type: ServiceAuthAction
        """

        self._allowed_actions = allowed_actions

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
        if issubclass(ServiceAuth, dict):
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
        if not isinstance(other, ServiceAuth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceAuth):
            return True

        return self.to_dict() != other.to_dict()
