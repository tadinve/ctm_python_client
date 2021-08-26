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


class Privileges(object):
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
        'client_access': 'ClientAccessPrivilegeCategory',
        'configuration_manager': 'ConfigurationManagerPrivilegeCategory',
        'monitoring': 'MonitoringPrivilegeCategory',
        'planning': 'PlanningPrivilegeCategory',
        'tools': 'ToolsPrivilegeCategory',
        'viewpoint_manager': 'ViewpointManagerPrivilegeCategory'
    }

    attribute_map = {
        'client_access': 'ClientAccess',
        'configuration_manager': 'ConfigurationManager',
        'monitoring': 'Monitoring',
        'planning': 'Planning',
        'tools': 'Tools',
        'viewpoint_manager': 'ViewpointManager'
    }

    def __init__(self, client_access=None, configuration_manager=None, monitoring=None, planning=None, tools=None, viewpoint_manager=None, _configuration=None):  # noqa: E501
        """Privileges - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_access = None
        self._configuration_manager = None
        self._monitoring = None
        self._planning = None
        self._tools = None
        self._viewpoint_manager = None
        self.discriminator = None

        if client_access is not None:
            self.client_access = client_access
        if configuration_manager is not None:
            self.configuration_manager = configuration_manager
        if monitoring is not None:
            self.monitoring = monitoring
        if planning is not None:
            self.planning = planning
        if tools is not None:
            self.tools = tools
        if viewpoint_manager is not None:
            self.viewpoint_manager = viewpoint_manager

    @property
    def client_access(self):
        """Gets the client_access of this Privileges.  # noqa: E501


        :return: The client_access of this Privileges.  # noqa: E501
        :rtype: ClientAccessPrivilegeCategory
        """
        return self._client_access

    @client_access.setter
    def client_access(self, client_access):
        """Sets the client_access of this Privileges.


        :param client_access: The client_access of this Privileges.  # noqa: E501
        :type: ClientAccessPrivilegeCategory
        """

        self._client_access = client_access

    @property
    def configuration_manager(self):
        """Gets the configuration_manager of this Privileges.  # noqa: E501


        :return: The configuration_manager of this Privileges.  # noqa: E501
        :rtype: ConfigurationManagerPrivilegeCategory
        """
        return self._configuration_manager

    @configuration_manager.setter
    def configuration_manager(self, configuration_manager):
        """Sets the configuration_manager of this Privileges.


        :param configuration_manager: The configuration_manager of this Privileges.  # noqa: E501
        :type: ConfigurationManagerPrivilegeCategory
        """

        self._configuration_manager = configuration_manager

    @property
    def monitoring(self):
        """Gets the monitoring of this Privileges.  # noqa: E501


        :return: The monitoring of this Privileges.  # noqa: E501
        :rtype: MonitoringPrivilegeCategory
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this Privileges.


        :param monitoring: The monitoring of this Privileges.  # noqa: E501
        :type: MonitoringPrivilegeCategory
        """

        self._monitoring = monitoring

    @property
    def planning(self):
        """Gets the planning of this Privileges.  # noqa: E501


        :return: The planning of this Privileges.  # noqa: E501
        :rtype: PlanningPrivilegeCategory
        """
        return self._planning

    @planning.setter
    def planning(self, planning):
        """Sets the planning of this Privileges.


        :param planning: The planning of this Privileges.  # noqa: E501
        :type: PlanningPrivilegeCategory
        """

        self._planning = planning

    @property
    def tools(self):
        """Gets the tools of this Privileges.  # noqa: E501


        :return: The tools of this Privileges.  # noqa: E501
        :rtype: ToolsPrivilegeCategory
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        """Sets the tools of this Privileges.


        :param tools: The tools of this Privileges.  # noqa: E501
        :type: ToolsPrivilegeCategory
        """

        self._tools = tools

    @property
    def viewpoint_manager(self):
        """Gets the viewpoint_manager of this Privileges.  # noqa: E501


        :return: The viewpoint_manager of this Privileges.  # noqa: E501
        :rtype: ViewpointManagerPrivilegeCategory
        """
        return self._viewpoint_manager

    @viewpoint_manager.setter
    def viewpoint_manager(self, viewpoint_manager):
        """Sets the viewpoint_manager of this Privileges.


        :param viewpoint_manager: The viewpoint_manager of this Privileges.  # noqa: E501
        :type: ViewpointManagerPrivilegeCategory
        """

        self._viewpoint_manager = viewpoint_manager

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
        if issubclass(Privileges, dict):
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
        if not isinstance(other, Privileges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Privileges):
            return True

        return self.to_dict() != other.to_dict()
