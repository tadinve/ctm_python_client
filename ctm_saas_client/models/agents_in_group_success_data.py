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


class AgentsInGroupSuccessData(object):
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
        'agents': 'list[AgentInGroupParams]'
    }

    attribute_map = {
        'message': 'message',
        'agents': 'agents'
    }

    def __init__(self, message=None, agents=None, _configuration=None):  # noqa: E501
        """AgentsInGroupSuccessData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._agents = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if agents is not None:
            self.agents = agents

    @property
    def message(self):
        """Gets the message of this AgentsInGroupSuccessData.  # noqa: E501

        The success message that describes the performed action.  # noqa: E501

        :return: The message of this AgentsInGroupSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AgentsInGroupSuccessData.

        The success message that describes the performed action.  # noqa: E501

        :param message: The message of this AgentsInGroupSuccessData.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def agents(self):
        """Gets the agents of this AgentsInGroupSuccessData.  # noqa: E501

        List of the items remained after the action.  # noqa: E501

        :return: The agents of this AgentsInGroupSuccessData.  # noqa: E501
        :rtype: list[AgentInGroupParams]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this AgentsInGroupSuccessData.

        List of the items remained after the action.  # noqa: E501

        :param agents: The agents of this AgentsInGroupSuccessData.  # noqa: E501
        :type: list[AgentInGroupParams]
        """

        self._agents = agents

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
        if issubclass(AgentsInGroupSuccessData, dict):
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
        if not isinstance(other, AgentsInGroupSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentsInGroupSuccessData):
            return True

        return self.to_dict() != other.to_dict()
