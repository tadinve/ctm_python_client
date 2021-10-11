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


class SettingProperties(object):
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
        'category': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'category': 'category',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, category=None, name=None, value=None, _configuration=None):  # noqa: E501
        """SettingProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._category = None
        self._name = None
        self._value = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def category(self):
        """Gets the category of this SettingProperties.  # noqa: E501

        setting category property HIDDEN  # noqa: E501

        :return: The category of this SettingProperties.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SettingProperties.

        setting category property HIDDEN  # noqa: E501

        :param category: The category of this SettingProperties.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def name(self):
        """Gets the name of this SettingProperties.  # noqa: E501

        setting name property HIDDEN  # noqa: E501

        :return: The name of this SettingProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SettingProperties.

        setting name property HIDDEN  # noqa: E501

        :param name: The name of this SettingProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this SettingProperties.  # noqa: E501

        setting value property HIDDEN  # noqa: E501

        :return: The value of this SettingProperties.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SettingProperties.

        setting value property HIDDEN  # noqa: E501

        :param value: The value of this SettingProperties.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(SettingProperties, dict):
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
        if not isinstance(other, SettingProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingProperties):
            return True

        return self.to_dict() != other.to_dict()
