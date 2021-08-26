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


class AgentSysParamSetSuccessData(object):
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
        'unsuccess_agents': 'list[AgentInfoResult]'
    }

    attribute_map = {
        'message': 'message',
        'unsuccess_agents': 'unsuccessAgents'
    }

    def __init__(self, message=None, unsuccess_agents=None, _configuration=None):  # noqa: E501
        """AgentSysParamSetSuccessData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._unsuccess_agents = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if unsuccess_agents is not None:
            self.unsuccess_agents = unsuccess_agents

    @property
    def message(self):
        """Gets the message of this AgentSysParamSetSuccessData.  # noqa: E501

        The success message that describes the action.  # noqa: E501

        :return: The message of this AgentSysParamSetSuccessData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AgentSysParamSetSuccessData.

        The success message that describes the action.  # noqa: E501

        :param message: The message of this AgentSysParamSetSuccessData.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def unsuccess_agents(self):
        """Gets the unsuccess_agents of this AgentSysParamSetSuccessData.  # noqa: E501

        List of the agents where parameter was not set.  # noqa: E501

        :return: The unsuccess_agents of this AgentSysParamSetSuccessData.  # noqa: E501
        :rtype: list[AgentInfoResult]
        """
        return self._unsuccess_agents

    @unsuccess_agents.setter
    def unsuccess_agents(self, unsuccess_agents):
        """Sets the unsuccess_agents of this AgentSysParamSetSuccessData.

        List of the agents where parameter was not set.  # noqa: E501

        :param unsuccess_agents: The unsuccess_agents of this AgentSysParamSetSuccessData.  # noqa: E501
        :type: list[AgentInfoResult]
        """

        self._unsuccess_agents = unsuccess_agents

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
        if issubclass(AgentSysParamSetSuccessData, dict):
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
        if not isinstance(other, AgentSysParamSetSuccessData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentSysParamSetSuccessData):
            return True

        return self.to_dict() != other.to_dict()
