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

from naga.ctm_api_client.configuration import Configuration


class AgentData(object):
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
        'name': 'str',
        'host': 'str',
        'node_id': 'str',
        'ctm': 'str',
        'ctm_host': 'str',
        'ctm_current_state': 'str',
        'current_state': 'str',
        'status': 'str',
        'status_message': 'str',
        'operating_system': 'str',
        'platform': 'str',
        'version': 'str',
        'last_update': 'str',
        'communication_version': 'str',
        'tag': 'str',
        'ssl_state': 'str',
        'host_groups': 'str',
        'plugins': 'list[PluginData]'
    }

    attribute_map = {
        'name': 'name',
        'host': 'host',
        'node_id': 'nodeID',
        'ctm': 'ctm',
        'ctm_host': 'ctmHost',
        'ctm_current_state': 'ctmCurrentState',
        'current_state': 'currentState',
        'status': 'status',
        'status_message': 'statusMessage',
        'operating_system': 'operatingSystem',
        'platform': 'platform',
        'version': 'version',
        'last_update': 'lastUpdate',
        'communication_version': 'communicationVersion',
        'tag': 'tag',
        'ssl_state': 'sslState',
        'host_groups': 'hostGroups',
        'plugins': 'plugins'
    }

    def __init__(self, name=None, host=None, node_id=None, ctm=None, ctm_host=None, ctm_current_state=None, current_state=None, status=None, status_message=None, operating_system=None, platform=None, version=None, last_update=None, communication_version=None, tag=None, ssl_state=None, host_groups=None, plugins=None, _configuration=None):  # noqa: E501
        """AgentData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._host = None
        self._node_id = None
        self._ctm = None
        self._ctm_host = None
        self._ctm_current_state = None
        self._current_state = None
        self._status = None
        self._status_message = None
        self._operating_system = None
        self._platform = None
        self._version = None
        self._last_update = None
        self._communication_version = None
        self._tag = None
        self._ssl_state = None
        self._host_groups = None
        self._plugins = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if node_id is not None:
            self.node_id = node_id
        if ctm is not None:
            self.ctm = ctm
        if ctm_host is not None:
            self.ctm_host = ctm_host
        if ctm_current_state is not None:
            self.ctm_current_state = ctm_current_state
        if current_state is not None:
            self.current_state = current_state
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if operating_system is not None:
            self.operating_system = operating_system
        if platform is not None:
            self.platform = platform
        if version is not None:
            self.version = version
        if last_update is not None:
            self.last_update = last_update
        if communication_version is not None:
            self.communication_version = communication_version
        if tag is not None:
            self.tag = tag
        if ssl_state is not None:
            self.ssl_state = ssl_state
        if host_groups is not None:
            self.host_groups = host_groups
        if plugins is not None:
            self.plugins = plugins

    @property
    def name(self):
        """Gets the name of this AgentData.  # noqa: E501

        The Agent name  # noqa: E501

        :return: The name of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentData.

        The Agent name  # noqa: E501

        :param name: The name of this AgentData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """Gets the host of this AgentData.  # noqa: E501

        The Agent host  # noqa: E501

        :return: The host of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AgentData.

        The Agent host  # noqa: E501

        :param host: The host of this AgentData.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def node_id(self):
        """Gets the node_id of this AgentData.  # noqa: E501

        The Agent nodeID  # noqa: E501

        :return: The node_id of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AgentData.

        The Agent nodeID  # noqa: E501

        :param node_id: The node_id of this AgentData.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def ctm(self):
        """Gets the ctm of this AgentData.  # noqa: E501

        The Control-M name  # noqa: E501

        :return: The ctm of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this AgentData.

        The Control-M name  # noqa: E501

        :param ctm: The ctm of this AgentData.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def ctm_host(self):
        """Gets the ctm_host of this AgentData.  # noqa: E501

        The Control-M Host  # noqa: E501

        :return: The ctm_host of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._ctm_host

    @ctm_host.setter
    def ctm_host(self, ctm_host):
        """Sets the ctm_host of this AgentData.

        The Control-M Host  # noqa: E501

        :param ctm_host: The ctm_host of this AgentData.  # noqa: E501
        :type: str
        """

        self._ctm_host = ctm_host

    @property
    def ctm_current_state(self):
        """Gets the ctm_current_state of this AgentData.  # noqa: E501

        The Control-M Host State  # noqa: E501

        :return: The ctm_current_state of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._ctm_current_state

    @ctm_current_state.setter
    def ctm_current_state(self, ctm_current_state):
        """Sets the ctm_current_state of this AgentData.

        The Control-M Host State  # noqa: E501

        :param ctm_current_state: The ctm_current_state of this AgentData.  # noqa: E501
        :type: str
        """

        self._ctm_current_state = ctm_current_state

    @property
    def current_state(self):
        """Gets the current_state of this AgentData.  # noqa: E501

        The Agent current state  # noqa: E501

        :return: The current_state of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """Sets the current_state of this AgentData.

        The Agent current state  # noqa: E501

        :param current_state: The current_state of this AgentData.  # noqa: E501
        :type: str
        """

        self._current_state = current_state

    @property
    def status(self):
        """Gets the status of this AgentData.  # noqa: E501

        The Agent status  # noqa: E501

        :return: The status of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AgentData.

        The Agent status  # noqa: E501

        :param status: The status of this AgentData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this AgentData.  # noqa: E501

        The Agent status message  # noqa: E501

        :return: The status_message of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this AgentData.

        The Agent status message  # noqa: E501

        :param status_message: The status_message of this AgentData.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def operating_system(self):
        """Gets the operating_system of this AgentData.  # noqa: E501

        The Agent operating System  # noqa: E501

        :return: The operating_system of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this AgentData.

        The Agent operating System  # noqa: E501

        :param operating_system: The operating_system of this AgentData.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def platform(self):
        """Gets the platform of this AgentData.  # noqa: E501

        The Agent platform  # noqa: E501

        :return: The platform of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this AgentData.

        The Agent platform  # noqa: E501

        :param platform: The platform of this AgentData.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def version(self):
        """Gets the version of this AgentData.  # noqa: E501

        The Agent version  # noqa: E501

        :return: The version of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AgentData.

        The Agent version  # noqa: E501

        :param version: The version of this AgentData.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def last_update(self):
        """Gets the last_update of this AgentData.  # noqa: E501

        The Agent last update  # noqa: E501

        :return: The last_update of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this AgentData.

        The Agent last update  # noqa: E501

        :param last_update: The last_update of this AgentData.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def communication_version(self):
        """Gets the communication_version of this AgentData.  # noqa: E501

        The Agent communication version  # noqa: E501

        :return: The communication_version of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._communication_version

    @communication_version.setter
    def communication_version(self, communication_version):
        """Sets the communication_version of this AgentData.

        The Agent communication version  # noqa: E501

        :param communication_version: The communication_version of this AgentData.  # noqa: E501
        :type: str
        """

        self._communication_version = communication_version

    @property
    def tag(self):
        """Gets the tag of this AgentData.  # noqa: E501

        The Agent tag  # noqa: E501

        :return: The tag of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AgentData.

        The Agent tag  # noqa: E501

        :param tag: The tag of this AgentData.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def ssl_state(self):
        """Gets the ssl_state of this AgentData.  # noqa: E501

        The Agent ssl state  # noqa: E501

        :return: The ssl_state of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._ssl_state

    @ssl_state.setter
    def ssl_state(self, ssl_state):
        """Sets the ssl_state of this AgentData.

        The Agent ssl state  # noqa: E501

        :param ssl_state: The ssl_state of this AgentData.  # noqa: E501
        :type: str
        """

        self._ssl_state = ssl_state

    @property
    def host_groups(self):
        """Gets the host_groups of this AgentData.  # noqa: E501

        The Agent host groups  # noqa: E501

        :return: The host_groups of this AgentData.  # noqa: E501
        :rtype: str
        """
        return self._host_groups

    @host_groups.setter
    def host_groups(self, host_groups):
        """Sets the host_groups of this AgentData.

        The Agent host groups  # noqa: E501

        :param host_groups: The host_groups of this AgentData.  # noqa: E501
        :type: str
        """

        self._host_groups = host_groups

    @property
    def plugins(self):
        """Gets the plugins of this AgentData.  # noqa: E501


        :return: The plugins of this AgentData.  # noqa: E501
        :rtype: list[PluginData]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this AgentData.


        :param plugins: The plugins of this AgentData.  # noqa: E501
        :type: list[PluginData]
        """

        self._plugins = plugins

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
        if issubclass(AgentData, dict):
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
        if not isinstance(other, AgentData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentData):
            return True

        return self.to_dict() != other.to_dict()
