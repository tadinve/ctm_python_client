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


class FtsSettingsData(object):
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
        'general_settings': 'FtsGeneralSettings',
        'ftp_settings': 'FtsFtpSettings',
        'sftp_settings': 'FtsSftpSettings',
        'authentication_details': 'FtsAuthenticationDetails'
    }

    attribute_map = {
        'general_settings': 'generalSettings',
        'ftp_settings': 'ftpSettings',
        'sftp_settings': 'sftpSettings',
        'authentication_details': 'authenticationDetails'
    }

    def __init__(self, general_settings=None, ftp_settings=None, sftp_settings=None, authentication_details=None, _configuration=None):  # noqa: E501
        """FtsSettingsData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._general_settings = None
        self._ftp_settings = None
        self._sftp_settings = None
        self._authentication_details = None
        self.discriminator = None

        if general_settings is not None:
            self.general_settings = general_settings
        if ftp_settings is not None:
            self.ftp_settings = ftp_settings
        if sftp_settings is not None:
            self.sftp_settings = sftp_settings
        if authentication_details is not None:
            self.authentication_details = authentication_details

    @property
    def general_settings(self):
        """Gets the general_settings of this FtsSettingsData.  # noqa: E501

        FTS general settings HIDDEN  # noqa: E501

        :return: The general_settings of this FtsSettingsData.  # noqa: E501
        :rtype: FtsGeneralSettings
        """
        return self._general_settings

    @general_settings.setter
    def general_settings(self, general_settings):
        """Sets the general_settings of this FtsSettingsData.

        FTS general settings HIDDEN  # noqa: E501

        :param general_settings: The general_settings of this FtsSettingsData.  # noqa: E501
        :type: FtsGeneralSettings
        """

        self._general_settings = general_settings

    @property
    def ftp_settings(self):
        """Gets the ftp_settings of this FtsSettingsData.  # noqa: E501

        FTS FTP settings HIDDEN  # noqa: E501

        :return: The ftp_settings of this FtsSettingsData.  # noqa: E501
        :rtype: FtsFtpSettings
        """
        return self._ftp_settings

    @ftp_settings.setter
    def ftp_settings(self, ftp_settings):
        """Sets the ftp_settings of this FtsSettingsData.

        FTS FTP settings HIDDEN  # noqa: E501

        :param ftp_settings: The ftp_settings of this FtsSettingsData.  # noqa: E501
        :type: FtsFtpSettings
        """

        self._ftp_settings = ftp_settings

    @property
    def sftp_settings(self):
        """Gets the sftp_settings of this FtsSettingsData.  # noqa: E501

        FTS SFTP settings HIDDEN  # noqa: E501

        :return: The sftp_settings of this FtsSettingsData.  # noqa: E501
        :rtype: FtsSftpSettings
        """
        return self._sftp_settings

    @sftp_settings.setter
    def sftp_settings(self, sftp_settings):
        """Sets the sftp_settings of this FtsSettingsData.

        FTS SFTP settings HIDDEN  # noqa: E501

        :param sftp_settings: The sftp_settings of this FtsSettingsData.  # noqa: E501
        :type: FtsSftpSettings
        """

        self._sftp_settings = sftp_settings

    @property
    def authentication_details(self):
        """Gets the authentication_details of this FtsSettingsData.  # noqa: E501

        FTS authentication details HIDDEN  # noqa: E501

        :return: The authentication_details of this FtsSettingsData.  # noqa: E501
        :rtype: FtsAuthenticationDetails
        """
        return self._authentication_details

    @authentication_details.setter
    def authentication_details(self, authentication_details):
        """Sets the authentication_details of this FtsSettingsData.

        FTS authentication details HIDDEN  # noqa: E501

        :param authentication_details: The authentication_details of this FtsSettingsData.  # noqa: E501
        :type: FtsAuthenticationDetails
        """

        self._authentication_details = authentication_details

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
        if issubclass(FtsSettingsData, dict):
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
        if not isinstance(other, FtsSettingsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FtsSettingsData):
            return True

        return self.to_dict() != other.to_dict()
