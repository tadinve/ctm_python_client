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


class AlertParam(object):
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
        'alert_ids': 'list[int]',
        'urgency': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'alert_ids': 'alertIds',
        'urgency': 'urgency',
        'comment': 'comment'
    }

    def __init__(self, alert_ids=None, urgency=None, comment=None, _configuration=None):  # noqa: E501
        """AlertParam - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_ids = None
        self._urgency = None
        self._comment = None
        self.discriminator = None

        self.alert_ids = alert_ids
        if urgency is not None:
            self.urgency = urgency
        if comment is not None:
            self.comment = comment

    @property
    def alert_ids(self):
        """Gets the alert_ids of this AlertParam.  # noqa: E501

        alertIds. HIDDEN.  # noqa: E501

        :return: The alert_ids of this AlertParam.  # noqa: E501
        :rtype: list[int]
        """
        return self._alert_ids

    @alert_ids.setter
    def alert_ids(self, alert_ids):
        """Sets the alert_ids of this AlertParam.

        alertIds. HIDDEN.  # noqa: E501

        :param alert_ids: The alert_ids of this AlertParam.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and alert_ids is None:
            raise ValueError("Invalid value for `alert_ids`, must not be `None`")  # noqa: E501

        self._alert_ids = alert_ids

    @property
    def urgency(self):
        """Gets the urgency of this AlertParam.  # noqa: E501

        modify urgency. HIDDEN.  # noqa: E501

        :return: The urgency of this AlertParam.  # noqa: E501
        :rtype: str
        """
        return self._urgency

    @urgency.setter
    def urgency(self, urgency):
        """Sets the urgency of this AlertParam.

        modify urgency. HIDDEN.  # noqa: E501

        :param urgency: The urgency of this AlertParam.  # noqa: E501
        :type: str
        """
        allowed_values = ["Normal", "Urgent", "Critical"]  # noqa: E501
        if (self._configuration.client_side_validation and
                urgency not in allowed_values):
            raise ValueError(
                "Invalid value for `urgency` ({0}), must be one of {1}"  # noqa: E501
                .format(urgency, allowed_values)
            )

        self._urgency = urgency

    @property
    def comment(self):
        """Gets the comment of this AlertParam.  # noqa: E501

        modify comment. HIDDEN.  # noqa: E501

        :return: The comment of this AlertParam.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AlertParam.

        modify comment. HIDDEN.  # noqa: E501

        :param comment: The comment of this AlertParam.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(AlertParam, dict):
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
        if not isinstance(other, AlertParam):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertParam):
            return True

        return self.to_dict() != other.to_dict()
