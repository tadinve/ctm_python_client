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


class AgentInGroupParamsList(object):
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
        'agentslist': 'list[AgentInGroupParams]'
    }

    attribute_map = {
        'agentslist': 'agentslist'
    }

    def __init__(self, agentslist=None, _configuration=None):  # noqa: E501
        """AgentInGroupParamsList - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agentslist = None
        self.discriminator = None

        if agentslist is not None:
            self.agentslist = agentslist

    @property
    def agentslist(self):
        """Gets the agentslist of this AgentInGroupParamsList.  # noqa: E501


        :return: The agentslist of this AgentInGroupParamsList.  # noqa: E501
        :rtype: list[AgentInGroupParams]
        """
        return self._agentslist

    @agentslist.setter
    def agentslist(self, agentslist):
        """Sets the agentslist of this AgentInGroupParamsList.


        :param agentslist: The agentslist of this AgentInGroupParamsList.  # noqa: E501
        :type: list[AgentInGroupParams]
        """

        self._agentslist = agentslist

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
        if issubclass(AgentInGroupParamsList, dict):
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
        if not isinstance(other, AgentInGroupParamsList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentInGroupParamsList):
            return True

        return self.to_dict() != other.to_dict()
