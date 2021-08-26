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


class JobtypeAgent(object):
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
        'server': 'str',
        'agent': 'str'
    }

    attribute_map = {
        'server': 'server',
        'agent': 'agent'
    }

    def __init__(self, server=None, agent=None, _configuration=None):  # noqa: E501
        """JobtypeAgent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._server = None
        self._agent = None
        self.discriminator = None

        if server is not None:
            self.server = server
        if agent is not None:
            self.agent = agent

    @property
    def server(self):
        """Gets the server of this JobtypeAgent.  # noqa: E501

        Server name  # noqa: E501

        :return: The server of this JobtypeAgent.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this JobtypeAgent.

        Server name  # noqa: E501

        :param server: The server of this JobtypeAgent.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def agent(self):
        """Gets the agent of this JobtypeAgent.  # noqa: E501

        Agent name  # noqa: E501

        :return: The agent of this JobtypeAgent.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this JobtypeAgent.

        Agent name  # noqa: E501

        :param agent: The agent of this JobtypeAgent.  # noqa: E501
        :type: str
        """

        self._agent = agent

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
        if issubclass(JobtypeAgent, dict):
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
        if not isinstance(other, JobtypeAgent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobtypeAgent):
            return True

        return self.to_dict() != other.to_dict()
