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


class StatisticsRunInfo(object):
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
        'average_info': 'StatisticsAverageInfo',
        'runs': 'list[StatisticsSingleRun]'
    }

    attribute_map = {
        'average_info': 'averageInfo',
        'runs': 'runs'
    }

    def __init__(self, average_info=None, runs=None, _configuration=None):  # noqa: E501
        """StatisticsRunInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._average_info = None
        self._runs = None
        self.discriminator = None

        if average_info is not None:
            self.average_info = average_info
        if runs is not None:
            self.runs = runs

    @property
    def average_info(self):
        """Gets the average_info of this StatisticsRunInfo.  # noqa: E501

        Statistics average information  # noqa: E501

        :return: The average_info of this StatisticsRunInfo.  # noqa: E501
        :rtype: StatisticsAverageInfo
        """
        return self._average_info

    @average_info.setter
    def average_info(self, average_info):
        """Sets the average_info of this StatisticsRunInfo.

        Statistics average information  # noqa: E501

        :param average_info: The average_info of this StatisticsRunInfo.  # noqa: E501
        :type: StatisticsAverageInfo
        """

        self._average_info = average_info

    @property
    def runs(self):
        """Gets the runs of this StatisticsRunInfo.  # noqa: E501


        :return: The runs of this StatisticsRunInfo.  # noqa: E501
        :rtype: list[StatisticsSingleRun]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this StatisticsRunInfo.


        :param runs: The runs of this StatisticsRunInfo.  # noqa: E501
        :type: list[StatisticsSingleRun]
        """

        self._runs = runs

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
        if issubclass(StatisticsRunInfo, dict):
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
        if not isinstance(other, StatisticsRunInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticsRunInfo):
            return True

        return self.to_dict() != other.to_dict()
