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


class WarningData(object):
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
        'id': 'str',
        'item': 'str',
        'file': 'str',
        'line': 'int',
        'col': 'int'
    }

    attribute_map = {
        'message': 'message',
        'id': 'id',
        'item': 'item',
        'file': 'file',
        'line': 'line',
        'col': 'col'
    }

    def __init__(self, message=None, id=None, item=None, file=None, line=None, col=None, _configuration=None):  # noqa: E501
        """WarningData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._id = None
        self._item = None
        self._file = None
        self._line = None
        self._col = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if id is not None:
            self.id = id
        if item is not None:
            self.item = item
        if file is not None:
            self.file = file
        if line is not None:
            self.line = line
        if col is not None:
            self.col = col

    @property
    def message(self):
        """Gets the message of this WarningData.  # noqa: E501

        The error message that describes the problem.  # noqa: E501

        :return: The message of this WarningData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WarningData.

        The error message that describes the problem.  # noqa: E501

        :param message: The message of this WarningData.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def id(self):
        """Gets the id of this WarningData.  # noqa: E501

        An internal identifier of the error.  # noqa: E501

        :return: The id of this WarningData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WarningData.

        An internal identifier of the error.  # noqa: E501

        :param id: The id of this WarningData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def item(self):
        """Gets the item of this WarningData.  # noqa: E501

        Reference to the item this error is referring to.  # noqa: E501

        :return: The item of this WarningData.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this WarningData.

        Reference to the item this error is referring to.  # noqa: E501

        :param item: The item of this WarningData.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def file(self):
        """Gets the file of this WarningData.  # noqa: E501

        The file this error occurred in.  # noqa: E501

        :return: The file of this WarningData.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this WarningData.

        The file this error occurred in.  # noqa: E501

        :param file: The file of this WarningData.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def line(self):
        """Gets the line of this WarningData.  # noqa: E501

        The number of line in the file this error occurred in.  # noqa: E501

        :return: The line of this WarningData.  # noqa: E501
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this WarningData.

        The number of line in the file this error occurred in.  # noqa: E501

        :param line: The line of this WarningData.  # noqa: E501
        :type: int
        """

        self._line = line

    @property
    def col(self):
        """Gets the col of this WarningData.  # noqa: E501

        The number of column in the file this error occurred in.  # noqa: E501

        :return: The col of this WarningData.  # noqa: E501
        :rtype: int
        """
        return self._col

    @col.setter
    def col(self, col):
        """Sets the col of this WarningData.

        The number of column in the file this error occurred in.  # noqa: E501

        :param col: The col of this WarningData.  # noqa: E501
        :type: int
        """

        self._col = col

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
        if issubclass(WarningData, dict):
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
        if not isinstance(other, WarningData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WarningData):
            return True

        return self.to_dict() != other.to_dict()
