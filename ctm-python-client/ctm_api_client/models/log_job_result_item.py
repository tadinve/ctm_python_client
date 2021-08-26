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

from ctm_python_client.ctm_api_client.configuration import Configuration


class LogJobResultItem(object):
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
        'data_arguments': 'list[LogDataArguments]',
        'formatted_message': 'str',
        'full_line': 'str',
        'local_timestamp_iso8601': 'str',
        'message': 'str',
        'message_code': 'str'
    }

    attribute_map = {
        'data_arguments': 'data_arguments',
        'formatted_message': 'formatted_message',
        'full_line': 'full_line',
        'local_timestamp_iso8601': 'local_timestamp_iso8601',
        'message': 'message',
        'message_code': 'message_code'
    }

    def __init__(self, data_arguments=None, formatted_message=None, full_line=None, local_timestamp_iso8601=None, message=None, message_code=None, _configuration=None):  # noqa: E501
        """LogJobResultItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_arguments = None
        self._formatted_message = None
        self._full_line = None
        self._local_timestamp_iso8601 = None
        self._message = None
        self._message_code = None
        self.discriminator = None

        if data_arguments is not None:
            self.data_arguments = data_arguments
        if formatted_message is not None:
            self.formatted_message = formatted_message
        if full_line is not None:
            self.full_line = full_line
        if local_timestamp_iso8601 is not None:
            self.local_timestamp_iso8601 = local_timestamp_iso8601
        if message is not None:
            self.message = message
        if message_code is not None:
            self.message_code = message_code

    @property
    def data_arguments(self):
        """Gets the data_arguments of this LogJobResultItem.  # noqa: E501


        :return: The data_arguments of this LogJobResultItem.  # noqa: E501
        :rtype: list[LogDataArguments]
        """
        return self._data_arguments

    @data_arguments.setter
    def data_arguments(self, data_arguments):
        """Sets the data_arguments of this LogJobResultItem.


        :param data_arguments: The data_arguments of this LogJobResultItem.  # noqa: E501
        :type: list[LogDataArguments]
        """

        self._data_arguments = data_arguments

    @property
    def formatted_message(self):
        """Gets the formatted_message of this LogJobResultItem.  # noqa: E501


        :return: The formatted_message of this LogJobResultItem.  # noqa: E501
        :rtype: str
        """
        return self._formatted_message

    @formatted_message.setter
    def formatted_message(self, formatted_message):
        """Sets the formatted_message of this LogJobResultItem.


        :param formatted_message: The formatted_message of this LogJobResultItem.  # noqa: E501
        :type: str
        """

        self._formatted_message = formatted_message

    @property
    def full_line(self):
        """Gets the full_line of this LogJobResultItem.  # noqa: E501


        :return: The full_line of this LogJobResultItem.  # noqa: E501
        :rtype: str
        """
        return self._full_line

    @full_line.setter
    def full_line(self, full_line):
        """Sets the full_line of this LogJobResultItem.


        :param full_line: The full_line of this LogJobResultItem.  # noqa: E501
        :type: str
        """

        self._full_line = full_line

    @property
    def local_timestamp_iso8601(self):
        """Gets the local_timestamp_iso8601 of this LogJobResultItem.  # noqa: E501


        :return: The local_timestamp_iso8601 of this LogJobResultItem.  # noqa: E501
        :rtype: str
        """
        return self._local_timestamp_iso8601

    @local_timestamp_iso8601.setter
    def local_timestamp_iso8601(self, local_timestamp_iso8601):
        """Sets the local_timestamp_iso8601 of this LogJobResultItem.


        :param local_timestamp_iso8601: The local_timestamp_iso8601 of this LogJobResultItem.  # noqa: E501
        :type: str
        """

        self._local_timestamp_iso8601 = local_timestamp_iso8601

    @property
    def message(self):
        """Gets the message of this LogJobResultItem.  # noqa: E501


        :return: The message of this LogJobResultItem.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LogJobResultItem.


        :param message: The message of this LogJobResultItem.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def message_code(self):
        """Gets the message_code of this LogJobResultItem.  # noqa: E501


        :return: The message_code of this LogJobResultItem.  # noqa: E501
        :rtype: str
        """
        return self._message_code

    @message_code.setter
    def message_code(self, message_code):
        """Sets the message_code of this LogJobResultItem.


        :param message_code: The message_code of this LogJobResultItem.  # noqa: E501
        :type: str
        """

        self._message_code = message_code

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
        if issubclass(LogJobResultItem, dict):
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
        if not isinstance(other, LogJobResultItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogJobResultItem):
            return True

        return self.to_dict() != other.to_dict()
