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


class AddRemoveSuccessData(object):
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
        'message': 'str',
        'current_items': 'list[str]'
    }

    attribute_map = {
        'message': 'message',
        'current_items': 'currentItems'
    }

    def __init__(self, message=None, current_items=None, _configuration=None):  # noqa: E501
        """AddRemoveSuccessData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._current_items = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if current_items is not None:
            self.current_items = current_items

    @property
    def message(self):
        """Gets the message of this AddRemoveSuccessData.  # noqa: E501

        The success message that describes the performed action.  # noqa: E501

        :return: The message of this AddRemoveSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AddRemoveSuccessData.

        The success message that describes the performed action.  # noqa: E501

        :param message: The message of this AddRemoveSuccessData.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def current_items(self):
        """Gets the current_items of this AddRemoveSuccessData.  # noqa: E501

        List of the items remained after the action.  # noqa: E501

        :return: The current_items of this AddRemoveSuccessData.  # noqa: E501
        :rtype: list[str]
        """
        return self._current_items

    @current_items.setter
    def current_items(self, current_items):
        """Sets the current_items of this AddRemoveSuccessData.

        List of the items remained after the action.  # noqa: E501

        :param current_items: The current_items of this AddRemoveSuccessData.  # noqa: E501
        :type: list[str]
        """

        self._current_items = current_items

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
        if issubclass(AddRemoveSuccessData, dict):
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
        if not isinstance(other, AddRemoveSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddRemoveSuccessData):
            return True

        return self.to_dict() != other.to_dict()
