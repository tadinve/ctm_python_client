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


class PluginData(object):
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
        'application_type': 'str',
        'application_version': 'str',
        'plugin_version': 'str',
        'version': 'str',
        'current_state': 'str',
        'status': 'str',
        'status_message': 'str',
        'last_update': 'str',
        'b2b_activated': 'str'
    }

    attribute_map = {
        'application_type': 'applicationType',
        'application_version': 'applicationVersion',
        'plugin_version': 'pluginVersion',
        'version': 'version',
        'current_state': 'currentState',
        'status': 'status',
        'status_message': 'statusMessage',
        'last_update': 'lastUpdate',
        'b2b_activated': 'b2bActivated'
    }

    def __init__(self, application_type=None, application_version=None, plugin_version=None, version=None, current_state=None, status=None, status_message=None, last_update=None, b2b_activated=None, _configuration=None):  # noqa: E501
        """PluginData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_type = None
        self._application_version = None
        self._plugin_version = None
        self._version = None
        self._current_state = None
        self._status = None
        self._status_message = None
        self._last_update = None
        self._b2b_activated = None
        self.discriminator = None

        if application_type is not None:
            self.application_type = application_type
        if application_version is not None:
            self.application_version = application_version
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if version is not None:
            self.version = version
        if current_state is not None:
            self.current_state = current_state
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if last_update is not None:
            self.last_update = last_update
        if b2b_activated is not None:
            self.b2b_activated = b2b_activated

    @property
    def application_type(self):
        """Gets the application_type of this PluginData.  # noqa: E501

        The application type  # noqa: E501

        :return: The application_type of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this PluginData.

        The application type  # noqa: E501

        :param application_type: The application_type of this PluginData.  # noqa: E501
        :type: str
        """

        self._application_type = application_type

    @property
    def application_version(self):
        """Gets the application_version of this PluginData.  # noqa: E501

        The application version  # noqa: E501

        :return: The application_version of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this PluginData.

        The application version  # noqa: E501

        :param application_version: The application_version of this PluginData.  # noqa: E501
        :type: str
        """

        self._application_version = application_version

    @property
    def plugin_version(self):
        """Gets the plugin_version of this PluginData.  # noqa: E501

        The plugin version  # noqa: E501

        :return: The plugin_version of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this PluginData.

        The plugin version  # noqa: E501

        :param plugin_version: The plugin_version of this PluginData.  # noqa: E501
        :type: str
        """

        self._plugin_version = plugin_version

    @property
    def version(self):
        """Gets the version of this PluginData.  # noqa: E501

        The version  # noqa: E501

        :return: The version of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PluginData.

        The version  # noqa: E501

        :param version: The version of this PluginData.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def current_state(self):
        """Gets the current_state of this PluginData.  # noqa: E501

        The current state  # noqa: E501

        :return: The current_state of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """Sets the current_state of this PluginData.

        The current state  # noqa: E501

        :param current_state: The current_state of this PluginData.  # noqa: E501
        :type: str
        """

        self._current_state = current_state

    @property
    def status(self):
        """Gets the status of this PluginData.  # noqa: E501

        The status  # noqa: E501

        :return: The status of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PluginData.

        The status  # noqa: E501

        :param status: The status of this PluginData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this PluginData.  # noqa: E501

        The status message  # noqa: E501

        :return: The status_message of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this PluginData.

        The status message  # noqa: E501

        :param status_message: The status_message of this PluginData.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def last_update(self):
        """Gets the last_update of this PluginData.  # noqa: E501

        The last update  # noqa: E501

        :return: The last_update of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this PluginData.

        The last update  # noqa: E501

        :param last_update: The last_update of this PluginData.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def b2b_activated(self):
        """Gets the b2b_activated of this PluginData.  # noqa: E501

        The B2B activated indication  # noqa: E501

        :return: The b2b_activated of this PluginData.  # noqa: E501
        :rtype: str
        """
        return self._b2b_activated

    @b2b_activated.setter
    def b2b_activated(self, b2b_activated):
        """Sets the b2b_activated of this PluginData.

        The B2B activated indication  # noqa: E501

        :param b2b_activated: The b2b_activated of this PluginData.  # noqa: E501
        :type: str
        """

        self._b2b_activated = b2b_activated

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
        if issubclass(PluginData, dict):
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
        if not isinstance(other, PluginData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginData):
            return True

        return self.to_dict() != other.to_dict()
