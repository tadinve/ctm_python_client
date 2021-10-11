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


class UserPreferences(object):
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
        'user_preferences': 'list[CTMNameValueSW]'
    }

    attribute_map = {
        'user_preferences': 'userPreferences'
    }

    def __init__(self, user_preferences=None, _configuration=None):  # noqa: E501
        """UserPreferences - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_preferences = None
        self.discriminator = None

        if user_preferences is not None:
            self.user_preferences = user_preferences

    @property
    def user_preferences(self):
        """Gets the user_preferences of this UserPreferences.  # noqa: E501

        The user preferences HIDDEN  # noqa: E501

        :return: The user_preferences of this UserPreferences.  # noqa: E501
        :rtype: list[CTMNameValueSW]
        """
        return self._user_preferences

    @user_preferences.setter
    def user_preferences(self, user_preferences):
        """Sets the user_preferences of this UserPreferences.

        The user preferences HIDDEN  # noqa: E501

        :param user_preferences: The user_preferences of this UserPreferences.  # noqa: E501
        :type: list[CTMNameValueSW]
        """

        self._user_preferences = user_preferences

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
        if issubclass(UserPreferences, dict):
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
        if not isinstance(other, UserPreferences):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPreferences):
            return True

        return self.to_dict() != other.to_dict()
