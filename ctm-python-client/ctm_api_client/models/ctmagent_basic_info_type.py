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


class CtmagentBasicInfoType(object):
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
        'server_to_agent_port_number': 'int',
        'agent_to_server_port_number': 'int',
        'persistent_connection': 'str',
        'tcpssl_server_mode': 'str',
        'protocol_version': 'str',
        'agent_status': 'str',
        'ip_addresses_list': 'list[str]'
    }

    attribute_map = {
        'server_to_agent_port_number': 'serverToAgentPortNumber',
        'agent_to_server_port_number': 'agentToServerPortNumber',
        'persistent_connection': 'persistentConnection',
        'tcpssl_server_mode': 'tcpsslServerMode',
        'protocol_version': 'protocolVersion',
        'agent_status': 'agentStatus',
        'ip_addresses_list': 'ipAddressesList'
    }

    def __init__(self, server_to_agent_port_number=None, agent_to_server_port_number=None, persistent_connection=None, tcpssl_server_mode=None, protocol_version=None, agent_status=None, ip_addresses_list=None, _configuration=None):  # noqa: E501
        """CtmagentBasicInfoType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._server_to_agent_port_number = None
        self._agent_to_server_port_number = None
        self._persistent_connection = None
        self._tcpssl_server_mode = None
        self._protocol_version = None
        self._agent_status = None
        self._ip_addresses_list = None
        self.discriminator = None

        if server_to_agent_port_number is not None:
            self.server_to_agent_port_number = server_to_agent_port_number
        if agent_to_server_port_number is not None:
            self.agent_to_server_port_number = agent_to_server_port_number
        if persistent_connection is not None:
            self.persistent_connection = persistent_connection
        if tcpssl_server_mode is not None:
            self.tcpssl_server_mode = tcpssl_server_mode
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if agent_status is not None:
            self.agent_status = agent_status
        if ip_addresses_list is not None:
            self.ip_addresses_list = ip_addresses_list

    @property
    def server_to_agent_port_number(self):
        """Gets the server_to_agent_port_number of this CtmagentBasicInfoType.  # noqa: E501

        server to agent port number  # noqa: E501

        :return: The server_to_agent_port_number of this CtmagentBasicInfoType.  # noqa: E501
        :rtype: int
        """
        return self._server_to_agent_port_number

    @server_to_agent_port_number.setter
    def server_to_agent_port_number(self, server_to_agent_port_number):
        """Sets the server_to_agent_port_number of this CtmagentBasicInfoType.

        server to agent port number  # noqa: E501

        :param server_to_agent_port_number: The server_to_agent_port_number of this CtmagentBasicInfoType.  # noqa: E501
        :type: int
        """

        self._server_to_agent_port_number = server_to_agent_port_number

    @property
    def agent_to_server_port_number(self):
        """Gets the agent_to_server_port_number of this CtmagentBasicInfoType.  # noqa: E501

        agent to server port number  # noqa: E501

        :return: The agent_to_server_port_number of this CtmagentBasicInfoType.  # noqa: E501
        :rtype: int
        """
        return self._agent_to_server_port_number

    @agent_to_server_port_number.setter
    def agent_to_server_port_number(self, agent_to_server_port_number):
        """Sets the agent_to_server_port_number of this CtmagentBasicInfoType.

        agent to server port number  # noqa: E501

        :param agent_to_server_port_number: The agent_to_server_port_number of this CtmagentBasicInfoType.  # noqa: E501
        :type: int
        """

        self._agent_to_server_port_number = agent_to_server_port_number

    @property
    def persistent_connection(self):
        """Gets the persistent_connection of this CtmagentBasicInfoType.  # noqa: E501

        is Server-Agent connection transient or perssistent  # noqa: E501

        :return: The persistent_connection of this CtmagentBasicInfoType.  # noqa: E501
        :rtype: str
        """
        return self._persistent_connection

    @persistent_connection.setter
    def persistent_connection(self, persistent_connection):
        """Sets the persistent_connection of this CtmagentBasicInfoType.

        is Server-Agent connection transient or perssistent  # noqa: E501

        :param persistent_connection: The persistent_connection of this CtmagentBasicInfoType.  # noqa: E501
        :type: str
        """

        self._persistent_connection = persistent_connection

    @property
    def tcpssl_server_mode(self):
        """Gets the tcpssl_server_mode of this CtmagentBasicInfoType.  # noqa: E501

        is connection TCP or SSL  # noqa: E501

        :return: The tcpssl_server_mode of this CtmagentBasicInfoType.  # noqa: E501
        :rtype: str
        """
        return self._tcpssl_server_mode

    @tcpssl_server_mode.setter
    def tcpssl_server_mode(self, tcpssl_server_mode):
        """Sets the tcpssl_server_mode of this CtmagentBasicInfoType.

        is connection TCP or SSL  # noqa: E501

        :param tcpssl_server_mode: The tcpssl_server_mode of this CtmagentBasicInfoType.  # noqa: E501
        :type: str
        """

        self._tcpssl_server_mode = tcpssl_server_mode

    @property
    def protocol_version(self):
        """Gets the protocol_version of this CtmagentBasicInfoType.  # noqa: E501

        communication protocol version of the Server-Agent  # noqa: E501

        :return: The protocol_version of this CtmagentBasicInfoType.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this CtmagentBasicInfoType.

        communication protocol version of the Server-Agent  # noqa: E501

        :param protocol_version: The protocol_version of this CtmagentBasicInfoType.  # noqa: E501
        :type: str
        """

        self._protocol_version = protocol_version

    @property
    def agent_status(self):
        """Gets the agent_status of this CtmagentBasicInfoType.  # noqa: E501

        the Agent's status message  # noqa: E501

        :return: The agent_status of this CtmagentBasicInfoType.  # noqa: E501
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this CtmagentBasicInfoType.

        the Agent's status message  # noqa: E501

        :param agent_status: The agent_status of this CtmagentBasicInfoType.  # noqa: E501
        :type: str
        """

        self._agent_status = agent_status

    @property
    def ip_addresses_list(self):
        """Gets the ip_addresses_list of this CtmagentBasicInfoType.  # noqa: E501


        :return: The ip_addresses_list of this CtmagentBasicInfoType.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses_list

    @ip_addresses_list.setter
    def ip_addresses_list(self, ip_addresses_list):
        """Sets the ip_addresses_list of this CtmagentBasicInfoType.


        :param ip_addresses_list: The ip_addresses_list of this CtmagentBasicInfoType.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses_list = ip_addresses_list

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
        if issubclass(CtmagentBasicInfoType, dict):
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
        if not isinstance(other, CtmagentBasicInfoType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CtmagentBasicInfoType):
            return True

        return self.to_dict() != other.to_dict()
