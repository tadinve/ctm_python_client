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


class AgentInGroupParams(object):
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
        'host': 'str',
        'hostgroup_agent_participation': 'HostgroupAgentParticipation'
    }

    attribute_map = {
        'host': 'host',
        'hostgroup_agent_participation': 'hostgroupAgentParticipation'
    }

    def __init__(self, host=None, hostgroup_agent_participation=None, _configuration=None):  # noqa: E501
        """AgentInGroupParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host = None
        self._hostgroup_agent_participation = None
        self.discriminator = None

        self.host = host
        if hostgroup_agent_participation is not None:
            self.hostgroup_agent_participation = hostgroup_agent_participation

    @property
    def host(self):
        """Gets the host of this AgentInGroupParams.  # noqa: E501

        The hostname of the agent.  # noqa: E501

        :return: The host of this AgentInGroupParams.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AgentInGroupParams.

        The hostname of the agent.  # noqa: E501

        :param host: The host of this AgentInGroupParams.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def hostgroup_agent_participation(self):
        """Gets the hostgroup_agent_participation of this AgentInGroupParams.  # noqa: E501

        The host condition. HIDDEN.  # noqa: E501

        :return: The hostgroup_agent_participation of this AgentInGroupParams.  # noqa: E501
        :rtype: HostgroupAgentParticipation
        """
        return self._hostgroup_agent_participation

    @hostgroup_agent_participation.setter
    def hostgroup_agent_participation(self, hostgroup_agent_participation):
        """Sets the hostgroup_agent_participation of this AgentInGroupParams.

        The host condition. HIDDEN.  # noqa: E501

        :param hostgroup_agent_participation: The hostgroup_agent_participation of this AgentInGroupParams.  # noqa: E501
        :type: HostgroupAgentParticipation
        """

        self._hostgroup_agent_participation = hostgroup_agent_participation

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
        if issubclass(AgentInGroupParams, dict):
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
        if not isinstance(other, AgentInGroupParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentInGroupParams):
            return True

        return self.to_dict() != other.to_dict()
