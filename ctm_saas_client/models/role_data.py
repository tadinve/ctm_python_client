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


class RoleData(object):
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
        'description': 'str',
        'organization_groups': 'list[str]',
        'organization_users': 'list[str]',
        'allowed_jobs': 'AllowedJobs',
        'allowed_job_actions': 'AllowedJobActions',
        'privileges': 'Privileges',
        'folders': 'list[FolderAuth]',
        'calendars': 'list[PrivilegeNameControlm]',
        'runas_users': 'list[RunasUserAuth]',
        'workload_policies': 'list[PrivilegeName]',
        'site_standard': 'list[PrivilegeName]',
        'site_customization': 'list[PrivilegeName]',
        'services': 'list[ServiceAuth]',
        'events': 'list[PrivilegeNameControlm]',
        'mutexes': 'list[PrivilegeNameControlm]',
        'locks': 'list[PrivilegeNameControlm]',
        'semaphores': 'list[PrivilegeNameControlm]',
        'pools': 'list[PrivilegeNameControlm]',
        'variables': 'list[PrivilegeNameControlm]',
        'global_events': 'list[PrivilegeName]',
        'agent_management': 'list[AgentMngAuth]',
        'plugin_management': 'list[PluginMngAuth]',
        'connection_profile_management': 'list[CPMngAuth]',
        'runas_definition_management': 'list[RunasDefinitionAuth]'
    }

    attribute_map = {
        'name': 'Name',
        'description': 'Description',
        'organization_groups': 'OrganizationGroups',
        'organization_users': 'OrganizationUsers',
        'allowed_jobs': 'AllowedJobs',
        'allowed_job_actions': 'AllowedJobActions',
        'privileges': 'Privileges',
        'folders': 'Folders',
        'calendars': 'Calendars',
        'runas_users': 'RunasUsers',
        'workload_policies': 'WorkloadPolicies',
        'site_standard': 'SiteStandard',
        'site_customization': 'SiteCustomization',
        'services': 'Services',
        'events': 'Events',
        'mutexes': 'Mutexes',
        'locks': 'Locks',
        'semaphores': 'Semaphores',
        'pools': 'Pools',
        'variables': 'Variables',
        'global_events': 'GlobalEvents',
        'agent_management': 'AgentManagement',
        'plugin_management': 'PluginManagement',
        'connection_profile_management': 'ConnectionProfileManagement',
        'runas_definition_management': 'RunasDefinitionManagement'
    }

    def __init__(self, name=None, description=None, organization_groups=None, organization_users=None, allowed_jobs=None, allowed_job_actions=None, privileges=None, folders=None, calendars=None, runas_users=None, workload_policies=None, site_standard=None, site_customization=None, services=None, events=None, mutexes=None, locks=None, semaphores=None, pools=None, variables=None, global_events=None, agent_management=None, plugin_management=None, connection_profile_management=None, runas_definition_management=None, _configuration=None):  # noqa: E501
        """RoleData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._organization_groups = None
        self._organization_users = None
        self._allowed_jobs = None
        self._allowed_job_actions = None
        self._privileges = None
        self._folders = None
        self._calendars = None
        self._runas_users = None
        self._workload_policies = None
        self._site_standard = None
        self._site_customization = None
        self._services = None
        self._events = None
        self._mutexes = None
        self._locks = None
        self._semaphores = None
        self._pools = None
        self._variables = None
        self._global_events = None
        self._agent_management = None
        self._plugin_management = None
        self._connection_profile_management = None
        self._runas_definition_management = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if organization_groups is not None:
            self.organization_groups = organization_groups
        if organization_users is not None:
            self.organization_users = organization_users
        if allowed_jobs is not None:
            self.allowed_jobs = allowed_jobs
        if allowed_job_actions is not None:
            self.allowed_job_actions = allowed_job_actions
        if privileges is not None:
            self.privileges = privileges
        if folders is not None:
            self.folders = folders
        if calendars is not None:
            self.calendars = calendars
        if runas_users is not None:
            self.runas_users = runas_users
        if workload_policies is not None:
            self.workload_policies = workload_policies
        if site_standard is not None:
            self.site_standard = site_standard
        if site_customization is not None:
            self.site_customization = site_customization
        if services is not None:
            self.services = services
        if events is not None:
            self.events = events
        if mutexes is not None:
            self.mutexes = mutexes
        if locks is not None:
            self.locks = locks
        if semaphores is not None:
            self.semaphores = semaphores
        if pools is not None:
            self.pools = pools
        if variables is not None:
            self.variables = variables
        if global_events is not None:
            self.global_events = global_events
        if agent_management is not None:
            self.agent_management = agent_management
        if plugin_management is not None:
            self.plugin_management = plugin_management
        if connection_profile_management is not None:
            self.connection_profile_management = connection_profile_management
        if runas_definition_management is not None:
            self.runas_definition_management = runas_definition_management

    @property
    def name(self):
        """Gets the name of this RoleData.  # noqa: E501

        role name  # noqa: E501

        :return: The name of this RoleData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleData.

        role name  # noqa: E501

        :param name: The name of this RoleData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RoleData.  # noqa: E501

        role description  # noqa: E501

        :return: The description of this RoleData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleData.

        role description  # noqa: E501

        :param description: The description of this RoleData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization_groups(self):
        """Gets the organization_groups of this RoleData.  # noqa: E501

        organization groups  # noqa: E501

        :return: The organization_groups of this RoleData.  # noqa: E501
        :rtype: list[str]
        """
        return self._organization_groups

    @organization_groups.setter
    def organization_groups(self, organization_groups):
        """Sets the organization_groups of this RoleData.

        organization groups  # noqa: E501

        :param organization_groups: The organization_groups of this RoleData.  # noqa: E501
        :type: list[str]
        """

        self._organization_groups = organization_groups

    @property
    def organization_users(self):
        """Gets the organization_users of this RoleData.  # noqa: E501

        organization usrs  # noqa: E501

        :return: The organization_users of this RoleData.  # noqa: E501
        :rtype: list[str]
        """
        return self._organization_users

    @organization_users.setter
    def organization_users(self, organization_users):
        """Sets the organization_users of this RoleData.

        organization usrs  # noqa: E501

        :param organization_users: The organization_users of this RoleData.  # noqa: E501
        :type: list[str]
        """

        self._organization_users = organization_users

    @property
    def allowed_jobs(self):
        """Gets the allowed_jobs of this RoleData.  # noqa: E501


        :return: The allowed_jobs of this RoleData.  # noqa: E501
        :rtype: AllowedJobs
        """
        return self._allowed_jobs

    @allowed_jobs.setter
    def allowed_jobs(self, allowed_jobs):
        """Sets the allowed_jobs of this RoleData.


        :param allowed_jobs: The allowed_jobs of this RoleData.  # noqa: E501
        :type: AllowedJobs
        """

        self._allowed_jobs = allowed_jobs

    @property
    def allowed_job_actions(self):
        """Gets the allowed_job_actions of this RoleData.  # noqa: E501


        :return: The allowed_job_actions of this RoleData.  # noqa: E501
        :rtype: AllowedJobActions
        """
        return self._allowed_job_actions

    @allowed_job_actions.setter
    def allowed_job_actions(self, allowed_job_actions):
        """Sets the allowed_job_actions of this RoleData.


        :param allowed_job_actions: The allowed_job_actions of this RoleData.  # noqa: E501
        :type: AllowedJobActions
        """

        self._allowed_job_actions = allowed_job_actions

    @property
    def privileges(self):
        """Gets the privileges of this RoleData.  # noqa: E501


        :return: The privileges of this RoleData.  # noqa: E501
        :rtype: Privileges
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this RoleData.


        :param privileges: The privileges of this RoleData.  # noqa: E501
        :type: Privileges
        """

        self._privileges = privileges

    @property
    def folders(self):
        """Gets the folders of this RoleData.  # noqa: E501


        :return: The folders of this RoleData.  # noqa: E501
        :rtype: list[FolderAuth]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this RoleData.


        :param folders: The folders of this RoleData.  # noqa: E501
        :type: list[FolderAuth]
        """

        self._folders = folders

    @property
    def calendars(self):
        """Gets the calendars of this RoleData.  # noqa: E501


        :return: The calendars of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeNameControlm]
        """
        return self._calendars

    @calendars.setter
    def calendars(self, calendars):
        """Sets the calendars of this RoleData.


        :param calendars: The calendars of this RoleData.  # noqa: E501
        :type: list[PrivilegeNameControlm]
        """

        self._calendars = calendars

    @property
    def runas_users(self):
        """Gets the runas_users of this RoleData.  # noqa: E501


        :return: The runas_users of this RoleData.  # noqa: E501
        :rtype: list[RunasUserAuth]
        """
        return self._runas_users

    @runas_users.setter
    def runas_users(self, runas_users):
        """Sets the runas_users of this RoleData.


        :param runas_users: The runas_users of this RoleData.  # noqa: E501
        :type: list[RunasUserAuth]
        """

        self._runas_users = runas_users

    @property
    def workload_policies(self):
        """Gets the workload_policies of this RoleData.  # noqa: E501


        :return: The workload_policies of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeName]
        """
        return self._workload_policies

    @workload_policies.setter
    def workload_policies(self, workload_policies):
        """Sets the workload_policies of this RoleData.


        :param workload_policies: The workload_policies of this RoleData.  # noqa: E501
        :type: list[PrivilegeName]
        """

        self._workload_policies = workload_policies

    @property
    def site_standard(self):
        """Gets the site_standard of this RoleData.  # noqa: E501


        :return: The site_standard of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeName]
        """
        return self._site_standard

    @site_standard.setter
    def site_standard(self, site_standard):
        """Sets the site_standard of this RoleData.


        :param site_standard: The site_standard of this RoleData.  # noqa: E501
        :type: list[PrivilegeName]
        """

        self._site_standard = site_standard

    @property
    def site_customization(self):
        """Gets the site_customization of this RoleData.  # noqa: E501


        :return: The site_customization of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeName]
        """
        return self._site_customization

    @site_customization.setter
    def site_customization(self, site_customization):
        """Sets the site_customization of this RoleData.


        :param site_customization: The site_customization of this RoleData.  # noqa: E501
        :type: list[PrivilegeName]
        """

        self._site_customization = site_customization

    @property
    def services(self):
        """Gets the services of this RoleData.  # noqa: E501


        :return: The services of this RoleData.  # noqa: E501
        :rtype: list[ServiceAuth]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this RoleData.


        :param services: The services of this RoleData.  # noqa: E501
        :type: list[ServiceAuth]
        """

        self._services = services

    @property
    def events(self):
        """Gets the events of this RoleData.  # noqa: E501


        :return: The events of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeNameControlm]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this RoleData.


        :param events: The events of this RoleData.  # noqa: E501
        :type: list[PrivilegeNameControlm]
        """

        self._events = events

    @property
    def mutexes(self):
        """Gets the mutexes of this RoleData.  # noqa: E501


        :return: The mutexes of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeNameControlm]
        """
        return self._mutexes

    @mutexes.setter
    def mutexes(self, mutexes):
        """Sets the mutexes of this RoleData.


        :param mutexes: The mutexes of this RoleData.  # noqa: E501
        :type: list[PrivilegeNameControlm]
        """

        self._mutexes = mutexes

    @property
    def locks(self):
        """Gets the locks of this RoleData.  # noqa: E501


        :return: The locks of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeNameControlm]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """Sets the locks of this RoleData.


        :param locks: The locks of this RoleData.  # noqa: E501
        :type: list[PrivilegeNameControlm]
        """

        self._locks = locks

    @property
    def semaphores(self):
        """Gets the semaphores of this RoleData.  # noqa: E501


        :return: The semaphores of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeNameControlm]
        """
        return self._semaphores

    @semaphores.setter
    def semaphores(self, semaphores):
        """Sets the semaphores of this RoleData.


        :param semaphores: The semaphores of this RoleData.  # noqa: E501
        :type: list[PrivilegeNameControlm]
        """

        self._semaphores = semaphores

    @property
    def pools(self):
        """Gets the pools of this RoleData.  # noqa: E501


        :return: The pools of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeNameControlm]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this RoleData.


        :param pools: The pools of this RoleData.  # noqa: E501
        :type: list[PrivilegeNameControlm]
        """

        self._pools = pools

    @property
    def variables(self):
        """Gets the variables of this RoleData.  # noqa: E501


        :return: The variables of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeNameControlm]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this RoleData.


        :param variables: The variables of this RoleData.  # noqa: E501
        :type: list[PrivilegeNameControlm]
        """

        self._variables = variables

    @property
    def global_events(self):
        """Gets the global_events of this RoleData.  # noqa: E501


        :return: The global_events of this RoleData.  # noqa: E501
        :rtype: list[PrivilegeName]
        """
        return self._global_events

    @global_events.setter
    def global_events(self, global_events):
        """Sets the global_events of this RoleData.


        :param global_events: The global_events of this RoleData.  # noqa: E501
        :type: list[PrivilegeName]
        """

        self._global_events = global_events

    @property
    def agent_management(self):
        """Gets the agent_management of this RoleData.  # noqa: E501


        :return: The agent_management of this RoleData.  # noqa: E501
        :rtype: list[AgentMngAuth]
        """
        return self._agent_management

    @agent_management.setter
    def agent_management(self, agent_management):
        """Sets the agent_management of this RoleData.


        :param agent_management: The agent_management of this RoleData.  # noqa: E501
        :type: list[AgentMngAuth]
        """

        self._agent_management = agent_management

    @property
    def plugin_management(self):
        """Gets the plugin_management of this RoleData.  # noqa: E501


        :return: The plugin_management of this RoleData.  # noqa: E501
        :rtype: list[PluginMngAuth]
        """
        return self._plugin_management

    @plugin_management.setter
    def plugin_management(self, plugin_management):
        """Sets the plugin_management of this RoleData.


        :param plugin_management: The plugin_management of this RoleData.  # noqa: E501
        :type: list[PluginMngAuth]
        """

        self._plugin_management = plugin_management

    @property
    def connection_profile_management(self):
        """Gets the connection_profile_management of this RoleData.  # noqa: E501


        :return: The connection_profile_management of this RoleData.  # noqa: E501
        :rtype: list[CPMngAuth]
        """
        return self._connection_profile_management

    @connection_profile_management.setter
    def connection_profile_management(self, connection_profile_management):
        """Sets the connection_profile_management of this RoleData.


        :param connection_profile_management: The connection_profile_management of this RoleData.  # noqa: E501
        :type: list[CPMngAuth]
        """

        self._connection_profile_management = connection_profile_management

    @property
    def runas_definition_management(self):
        """Gets the runas_definition_management of this RoleData.  # noqa: E501


        :return: The runas_definition_management of this RoleData.  # noqa: E501
        :rtype: list[RunasDefinitionAuth]
        """
        return self._runas_definition_management

    @runas_definition_management.setter
    def runas_definition_management(self, runas_definition_management):
        """Sets the runas_definition_management of this RoleData.


        :param runas_definition_management: The runas_definition_management of this RoleData.  # noqa: E501
        :type: list[RunasDefinitionAuth]
        """

        self._runas_definition_management = runas_definition_management

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
        if issubclass(RoleData, dict):
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
        if not isinstance(other, RoleData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleData):
            return True

        return self.to_dict() != other.to_dict()
