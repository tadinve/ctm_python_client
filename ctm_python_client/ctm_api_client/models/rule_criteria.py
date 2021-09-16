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


class RuleCriteria(object):
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
    swagger_types = {"field": "str", "criteria": "str", "exceptions": "list[str]"}

    attribute_map = {
        "field": "field",
        "criteria": "criteria",
        "exceptions": "exceptions",
    }

    def __init__(
        self, field=None, criteria=None, exceptions=None, _configuration=None
    ):  # noqa: E501
        """RuleCriteria - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._field = None
        self._criteria = None
        self._exceptions = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if criteria is not None:
            self.criteria = criteria
        if exceptions is not None:
            self.exceptions = exceptions

    @property
    def field(self):
        """Gets the field of this RuleCriteria.  # noqa: E501

        Rule parameters fields can be one of the options - ctm, type, jobName, jobType, application, subApplication, jobStatus, folder and library. HIDDEN.  # noqa: E501

        :return: The field of this RuleCriteria.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this RuleCriteria.

        Rule parameters fields can be one of the options - ctm, type, jobName, jobType, application, subApplication, jobStatus, folder and library. HIDDEN.  # noqa: E501

        :param field: The field of this RuleCriteria.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def criteria(self):
        """Gets the criteria of this RuleCriteria.  # noqa: E501


        :return: The criteria of this RuleCriteria.  # noqa: E501
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this RuleCriteria.


        :param criteria: The criteria of this RuleCriteria.  # noqa: E501
        :type: str
        """

        self._criteria = criteria

    @property
    def exceptions(self):
        """Gets the exceptions of this RuleCriteria.  # noqa: E501


        :return: The exceptions of this RuleCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._exceptions

    @exceptions.setter
    def exceptions(self, exceptions):
        """Sets the exceptions of this RuleCriteria.


        :param exceptions: The exceptions of this RuleCriteria.  # noqa: E501
        :type: list[str]
        """

        self._exceptions = exceptions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(RuleCriteria, dict):
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
        if not isinstance(other, RuleCriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuleCriteria):
            return True

        return self.to_dict() != other.to_dict()
