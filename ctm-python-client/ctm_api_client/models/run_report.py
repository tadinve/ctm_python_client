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


class RunReport(object):
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
        'format': 'str',
        'filters': 'ReportFilters',
        'date_time_settings': 'ReportDateTimeSettings'
    }

    attribute_map = {
        'name': 'name',
        'format': 'format',
        'filters': 'filters',
        'date_time_settings': 'dateTimeSettings'
    }

    def __init__(self, name=None, format=None, filters=None, date_time_settings=None, _configuration=None):  # noqa: E501
        """RunReport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._format = None
        self._filters = None
        self._date_time_settings = None
        self.discriminator = None

        self.name = name
        if format is not None:
            self.format = format
        if filters is not None:
            self.filters = filters
        if date_time_settings is not None:
            self.date_time_settings = date_time_settings

    @property
    def name(self):
        """Gets the name of this RunReport.  # noqa: E501


        :return: The name of this RunReport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RunReport.


        :param name: The name of this RunReport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def format(self):
        """Gets the format of this RunReport.  # noqa: E501


        :return: The format of this RunReport.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RunReport.


        :param format: The format of this RunReport.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def filters(self):
        """Gets the filters of this RunReport.  # noqa: E501

        HIDDEN.  # noqa: E501

        :return: The filters of this RunReport.  # noqa: E501
        :rtype: ReportFilters
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this RunReport.

        HIDDEN.  # noqa: E501

        :param filters: The filters of this RunReport.  # noqa: E501
        :type: ReportFilters
        """

        self._filters = filters

    @property
    def date_time_settings(self):
        """Gets the date_time_settings of this RunReport.  # noqa: E501

        HIDDEN.  # noqa: E501

        :return: The date_time_settings of this RunReport.  # noqa: E501
        :rtype: ReportDateTimeSettings
        """
        return self._date_time_settings

    @date_time_settings.setter
    def date_time_settings(self, date_time_settings):
        """Sets the date_time_settings of this RunReport.

        HIDDEN.  # noqa: E501

        :param date_time_settings: The date_time_settings of this RunReport.  # noqa: E501
        :type: ReportDateTimeSettings
        """

        self._date_time_settings = date_time_settings

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
        if issubclass(RunReport, dict):
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
        if not isinstance(other, RunReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunReport):
            return True

        return self.to_dict() != other.to_dict()
