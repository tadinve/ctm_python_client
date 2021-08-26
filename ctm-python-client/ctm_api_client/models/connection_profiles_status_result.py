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


class ConnectionProfilesStatusResult(object):
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
        'statuses': 'list[ConnectionProfileStatus]',
        'returned': 'int',
        'total': 'int'
    }

    attribute_map = {
        'statuses': 'statuses',
        'returned': 'returned',
        'total': 'total'
    }

    def __init__(self, statuses=None, returned=None, total=None, _configuration=None):  # noqa: E501
        """ConnectionProfilesStatusResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._statuses = None
        self._returned = None
        self._total = None
        self.discriminator = None

        if statuses is not None:
            self.statuses = statuses
        if returned is not None:
            self.returned = returned
        if total is not None:
            self.total = total

    @property
    def statuses(self):
        """Gets the statuses of this ConnectionProfilesStatusResult.  # noqa: E501

        The list of statuses tracked by the given runId.  # noqa: E501

        :return: The statuses of this ConnectionProfilesStatusResult.  # noqa: E501
        :rtype: list[ConnectionProfileStatus]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this ConnectionProfilesStatusResult.

        The list of statuses tracked by the given runId.  # noqa: E501

        :param statuses: The statuses of this ConnectionProfilesStatusResult.  # noqa: E501
        :type: list[ConnectionProfileStatus]
        """

        self._statuses = statuses

    @property
    def returned(self):
        """Gets the returned of this ConnectionProfilesStatusResult.  # noqa: E501

        The number of the return items by the search.  # noqa: E501

        :return: The returned of this ConnectionProfilesStatusResult.  # noqa: E501
        :rtype: int
        """
        return self._returned

    @returned.setter
    def returned(self, returned):
        """Sets the returned of this ConnectionProfilesStatusResult.

        The number of the return items by the search.  # noqa: E501

        :param returned: The returned of this ConnectionProfilesStatusResult.  # noqa: E501
        :type: int
        """

        self._returned = returned

    @property
    def total(self):
        """Gets the total of this ConnectionProfilesStatusResult.  # noqa: E501

        The total number of items.  # noqa: E501

        :return: The total of this ConnectionProfilesStatusResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ConnectionProfilesStatusResult.

        The total number of items.  # noqa: E501

        :param total: The total of this ConnectionProfilesStatusResult.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(ConnectionProfilesStatusResult, dict):
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
        if not isinstance(other, ConnectionProfilesStatusResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionProfilesStatusResult):
            return True

        return self.to_dict() != other.to_dict()
