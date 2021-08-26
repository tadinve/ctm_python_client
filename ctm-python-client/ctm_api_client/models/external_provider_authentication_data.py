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


class ExternalProviderAuthenticationData(object):
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
        'ldap_user_and_domain': 'str'
    }

    attribute_map = {
        'ldap_user_and_domain': 'LdapUserAndDomain'
    }

    def __init__(self, ldap_user_and_domain=None, _configuration=None):  # noqa: E501
        """ExternalProviderAuthenticationData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ldap_user_and_domain = None
        self.discriminator = None

        if ldap_user_and_domain is not None:
            self.ldap_user_and_domain = ldap_user_and_domain

    @property
    def ldap_user_and_domain(self):
        """Gets the ldap_user_and_domain of this ExternalProviderAuthenticationData.  # noqa: E501

        ldap user and domain  # noqa: E501

        :return: The ldap_user_and_domain of this ExternalProviderAuthenticationData.  # noqa: E501
        :rtype: str
        """
        return self._ldap_user_and_domain

    @ldap_user_and_domain.setter
    def ldap_user_and_domain(self, ldap_user_and_domain):
        """Sets the ldap_user_and_domain of this ExternalProviderAuthenticationData.

        ldap user and domain  # noqa: E501

        :param ldap_user_and_domain: The ldap_user_and_domain of this ExternalProviderAuthenticationData.  # noqa: E501
        :type: str
        """

        self._ldap_user_and_domain = ldap_user_and_domain

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
        if issubclass(ExternalProviderAuthenticationData, dict):
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
        if not isinstance(other, ExternalProviderAuthenticationData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalProviderAuthenticationData):
            return True

        return self.to_dict() != other.to_dict()
