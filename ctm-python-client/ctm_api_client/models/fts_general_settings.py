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


class FtsGeneralSettings(object):
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
        'home_directory': 'str',
        'multiple_login_allowed': 'bool',
        'max_open_sessions': 'int',
        'max_login_failures': 'int',
        'delay_after_login_failure': 'int',
        'throttling_activated': 'bool',
        'max_simultaneous_uploads': 'int',
        'max_simultaneous_downloads': 'int',
        'server_enabled': 'bool'
    }

    attribute_map = {
        'home_directory': 'homeDirectory',
        'multiple_login_allowed': 'multipleLoginAllowed',
        'max_open_sessions': 'maxOpenSessions',
        'max_login_failures': 'maxLoginFailures',
        'delay_after_login_failure': 'delayAfterLoginFailure',
        'throttling_activated': 'throttlingActivated',
        'max_simultaneous_uploads': 'maxSimultaneousUploads',
        'max_simultaneous_downloads': 'maxSimultaneousDownloads',
        'server_enabled': 'serverEnabled'
    }

    def __init__(self, home_directory=None, multiple_login_allowed=None, max_open_sessions=None, max_login_failures=None, delay_after_login_failure=None, throttling_activated=None, max_simultaneous_uploads=None, max_simultaneous_downloads=None, server_enabled=None, _configuration=None):  # noqa: E501
        """FtsGeneralSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._home_directory = None
        self._multiple_login_allowed = None
        self._max_open_sessions = None
        self._max_login_failures = None
        self._delay_after_login_failure = None
        self._throttling_activated = None
        self._max_simultaneous_uploads = None
        self._max_simultaneous_downloads = None
        self._server_enabled = None
        self.discriminator = None

        if home_directory is not None:
            self.home_directory = home_directory
        if multiple_login_allowed is not None:
            self.multiple_login_allowed = multiple_login_allowed
        if max_open_sessions is not None:
            self.max_open_sessions = max_open_sessions
        if max_login_failures is not None:
            self.max_login_failures = max_login_failures
        if delay_after_login_failure is not None:
            self.delay_after_login_failure = delay_after_login_failure
        if throttling_activated is not None:
            self.throttling_activated = throttling_activated
        if max_simultaneous_uploads is not None:
            self.max_simultaneous_uploads = max_simultaneous_uploads
        if max_simultaneous_downloads is not None:
            self.max_simultaneous_downloads = max_simultaneous_downloads
        if server_enabled is not None:
            self.server_enabled = server_enabled

    @property
    def home_directory(self):
        """Gets the home_directory of this FtsGeneralSettings.  # noqa: E501

        Root path where transferred files are stored. If you want to use a different directory for each logged in user, you must add /${userName} to the path.  # noqa: E501

        :return: The home_directory of this FtsGeneralSettings.  # noqa: E501
        :rtype: str
        """
        return self._home_directory

    @home_directory.setter
    def home_directory(self, home_directory):
        """Sets the home_directory of this FtsGeneralSettings.

        Root path where transferred files are stored. If you want to use a different directory for each logged in user, you must add /${userName} to the path.  # noqa: E501

        :param home_directory: The home_directory of this FtsGeneralSettings.  # noqa: E501
        :type: str
        """

        self._home_directory = home_directory

    @property
    def multiple_login_allowed(self):
        """Gets the multiple_login_allowed of this FtsGeneralSettings.  # noqa: E501

        Allow multiple open sessions  # noqa: E501

        :return: The multiple_login_allowed of this FtsGeneralSettings.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_login_allowed

    @multiple_login_allowed.setter
    def multiple_login_allowed(self, multiple_login_allowed):
        """Sets the multiple_login_allowed of this FtsGeneralSettings.

        Allow multiple open sessions  # noqa: E501

        :param multiple_login_allowed: The multiple_login_allowed of this FtsGeneralSettings.  # noqa: E501
        :type: bool
        """

        self._multiple_login_allowed = multiple_login_allowed

    @property
    def max_open_sessions(self):
        """Gets the max_open_sessions of this FtsGeneralSettings.  # noqa: E501

        Maximum concurrent open sessions  # noqa: E501

        :return: The max_open_sessions of this FtsGeneralSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_open_sessions

    @max_open_sessions.setter
    def max_open_sessions(self, max_open_sessions):
        """Sets the max_open_sessions of this FtsGeneralSettings.

        Maximum concurrent open sessions  # noqa: E501

        :param max_open_sessions: The max_open_sessions of this FtsGeneralSettings.  # noqa: E501
        :type: int
        """

        self._max_open_sessions = max_open_sessions

    @property
    def max_login_failures(self):
        """Gets the max_login_failures of this FtsGeneralSettings.  # noqa: E501

        Number of retries before the server closes the connection  # noqa: E501

        :return: The max_login_failures of this FtsGeneralSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_login_failures

    @max_login_failures.setter
    def max_login_failures(self, max_login_failures):
        """Sets the max_login_failures of this FtsGeneralSettings.

        Number of retries before the server closes the connection  # noqa: E501

        :param max_login_failures: The max_login_failures of this FtsGeneralSettings.  # noqa: E501
        :type: int
        """

        self._max_login_failures = max_login_failures

    @property
    def delay_after_login_failure(self):
        """Gets the delay_after_login_failure of this FtsGeneralSettings.  # noqa: E501

        Time of waiting before letting the user to do another login in seconds  # noqa: E501

        :return: The delay_after_login_failure of this FtsGeneralSettings.  # noqa: E501
        :rtype: int
        """
        return self._delay_after_login_failure

    @delay_after_login_failure.setter
    def delay_after_login_failure(self, delay_after_login_failure):
        """Sets the delay_after_login_failure of this FtsGeneralSettings.

        Time of waiting before letting the user to do another login in seconds  # noqa: E501

        :param delay_after_login_failure: The delay_after_login_failure of this FtsGeneralSettings.  # noqa: E501
        :type: int
        """

        self._delay_after_login_failure = delay_after_login_failure

    @property
    def throttling_activated(self):
        """Gets the throttling_activated of this FtsGeneralSettings.  # noqa: E501

        Allow bandwidth throttling  # noqa: E501

        :return: The throttling_activated of this FtsGeneralSettings.  # noqa: E501
        :rtype: bool
        """
        return self._throttling_activated

    @throttling_activated.setter
    def throttling_activated(self, throttling_activated):
        """Sets the throttling_activated of this FtsGeneralSettings.

        Allow bandwidth throttling  # noqa: E501

        :param throttling_activated: The throttling_activated of this FtsGeneralSettings.  # noqa: E501
        :type: bool
        """

        self._throttling_activated = throttling_activated

    @property
    def max_simultaneous_uploads(self):
        """Gets the max_simultaneous_uploads of this FtsGeneralSettings.  # noqa: E501

        Maximum simultaneos uploads  # noqa: E501

        :return: The max_simultaneous_uploads of this FtsGeneralSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_simultaneous_uploads

    @max_simultaneous_uploads.setter
    def max_simultaneous_uploads(self, max_simultaneous_uploads):
        """Sets the max_simultaneous_uploads of this FtsGeneralSettings.

        Maximum simultaneos uploads  # noqa: E501

        :param max_simultaneous_uploads: The max_simultaneous_uploads of this FtsGeneralSettings.  # noqa: E501
        :type: int
        """

        self._max_simultaneous_uploads = max_simultaneous_uploads

    @property
    def max_simultaneous_downloads(self):
        """Gets the max_simultaneous_downloads of this FtsGeneralSettings.  # noqa: E501

        Maximum simultaneos downloads  # noqa: E501

        :return: The max_simultaneous_downloads of this FtsGeneralSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_simultaneous_downloads

    @max_simultaneous_downloads.setter
    def max_simultaneous_downloads(self, max_simultaneous_downloads):
        """Sets the max_simultaneous_downloads of this FtsGeneralSettings.

        Maximum simultaneos downloads  # noqa: E501

        :param max_simultaneous_downloads: The max_simultaneous_downloads of this FtsGeneralSettings.  # noqa: E501
        :type: int
        """

        self._max_simultaneous_downloads = max_simultaneous_downloads

    @property
    def server_enabled(self):
        """Gets the server_enabled of this FtsGeneralSettings.  # noqa: E501

        Enable/Disable the File Transfer Server  # noqa: E501

        :return: The server_enabled of this FtsGeneralSettings.  # noqa: E501
        :rtype: bool
        """
        return self._server_enabled

    @server_enabled.setter
    def server_enabled(self, server_enabled):
        """Sets the server_enabled of this FtsGeneralSettings.

        Enable/Disable the File Transfer Server  # noqa: E501

        :param server_enabled: The server_enabled of this FtsGeneralSettings.  # noqa: E501
        :type: bool
        """

        self._server_enabled = server_enabled

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
        if issubclass(FtsGeneralSettings, dict):
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
        if not isinstance(other, FtsGeneralSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FtsGeneralSettings):
            return True

        return self.to_dict() != other.to_dict()
