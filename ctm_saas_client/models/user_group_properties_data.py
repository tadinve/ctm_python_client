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


class UserGroupPropertiesData(object):
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
        'external_users': 'list[str]',
        'ldap_groups': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'external_users': 'externalUsers',
        'ldap_groups': 'ldapGroups'
    }

    def __init__(self, name=None, external_users=None, ldap_groups=None, _configuration=None):  # noqa: E501
        """UserGroupPropertiesData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._external_users = None
        self._ldap_groups = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if external_users is not None:
            self.external_users = external_users
        if ldap_groups is not None:
            self.ldap_groups = ldap_groups

    @property
    def name(self):
        """Gets the name of this UserGroupPropertiesData.  # noqa: E501

        user group name REQUIRED  # noqa: E501

        :return: The name of this UserGroupPropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserGroupPropertiesData.

        user group name REQUIRED  # noqa: E501

        :param name: The name of this UserGroupPropertiesData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def external_users(self):
        """Gets the external_users of this UserGroupPropertiesData.  # noqa: E501

        external users HIDDEN  # noqa: E501

        :return: The external_users of this UserGroupPropertiesData.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_users

    @external_users.setter
    def external_users(self, external_users):
        """Sets the external_users of this UserGroupPropertiesData.

        external users HIDDEN  # noqa: E501

        :param external_users: The external_users of this UserGroupPropertiesData.  # noqa: E501
        :type: list[str]
        """

        self._external_users = external_users

    @property
    def ldap_groups(self):
        """Gets the ldap_groups of this UserGroupPropertiesData.  # noqa: E501

        ldap groups HIDDEN  # noqa: E501

        :return: The ldap_groups of this UserGroupPropertiesData.  # noqa: E501
        :rtype: list[str]
        """
        return self._ldap_groups

    @ldap_groups.setter
    def ldap_groups(self, ldap_groups):
        """Sets the ldap_groups of this UserGroupPropertiesData.

        ldap groups HIDDEN  # noqa: E501

        :param ldap_groups: The ldap_groups of this UserGroupPropertiesData.  # noqa: E501
        :type: list[str]
        """

        self._ldap_groups = ldap_groups

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
        if issubclass(UserGroupPropertiesData, dict):
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
        if not isinstance(other, UserGroupPropertiesData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserGroupPropertiesData):
            return True

        return self.to_dict() != other.to_dict()
