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


class Event(object):
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
    swagger_types = {"name": "str", "ctm": "str", "_date": "str"}

    attribute_map = {"name": "name", "ctm": "ctm", "_date": "date"}

    def __init__(
        self, name=None, ctm=None, _date=None, _configuration=None
    ):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._ctm = None
        self.__date = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ctm is not None:
            self.ctm = ctm
        if _date is not None:
            self._date = _date

    @property
    def name(self):
        """Gets the name of this Event.  # noqa: E501

        Event name  # noqa: E501

        :return: The name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Event.

        Event name  # noqa: E501

        :param name: The name of this Event.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ctm(self):
        """Gets the ctm of this Event.  # noqa: E501

        Control-M Server hosting the event  # noqa: E501

        :return: The ctm of this Event.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this Event.

        Control-M Server hosting the event  # noqa: E501

        :param ctm: The ctm of this Event.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def _date(self):
        """Gets the _date of this Event.  # noqa: E501

        The event date, either date in format dd/mm/yy or a string \"orderdate\"  # noqa: E501

        :return: The _date of this Event.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Event.

        The event date, either date in format dd/mm/yy or a string \"orderdate\"  # noqa: E501

        :param _date: The _date of this Event.  # noqa: E501
        :type: str
        """

        self.__date = _date

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Event):
            return True

        return self.to_dict() != other.to_dict()
