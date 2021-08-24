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


class MFTEntitiesListNames(object):
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
        'users': 'list[str]',
        'virtual_folders': 'list[str]',
        'groups': 'list[str]',
        'company_names': 'list[str]'
    }

    attribute_map = {
        'users': 'users',
        'virtual_folders': 'virtualFolders',
        'groups': 'groups',
        'company_names': 'companyNames'
    }

    def __init__(self, users=None, virtual_folders=None, groups=None, company_names=None, _configuration=None):  # noqa: E501
        """MFTEntitiesListNames - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._users = None
        self._virtual_folders = None
        self._groups = None
        self._company_names = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if virtual_folders is not None:
            self.virtual_folders = virtual_folders
        if groups is not None:
            self.groups = groups
        if company_names is not None:
            self.company_names = company_names

    @property
    def users(self):
        """Gets the users of this MFTEntitiesListNames.  # noqa: E501


        :return: The users of this MFTEntitiesListNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this MFTEntitiesListNames.


        :param users: The users of this MFTEntitiesListNames.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def virtual_folders(self):
        """Gets the virtual_folders of this MFTEntitiesListNames.  # noqa: E501


        :return: The virtual_folders of this MFTEntitiesListNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._virtual_folders

    @virtual_folders.setter
    def virtual_folders(self, virtual_folders):
        """Sets the virtual_folders of this MFTEntitiesListNames.


        :param virtual_folders: The virtual_folders of this MFTEntitiesListNames.  # noqa: E501
        :type: list[str]
        """

        self._virtual_folders = virtual_folders

    @property
    def groups(self):
        """Gets the groups of this MFTEntitiesListNames.  # noqa: E501


        :return: The groups of this MFTEntitiesListNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this MFTEntitiesListNames.


        :param groups: The groups of this MFTEntitiesListNames.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def company_names(self):
        """Gets the company_names of this MFTEntitiesListNames.  # noqa: E501


        :return: The company_names of this MFTEntitiesListNames.  # noqa: E501
        :rtype: list[str]
        """
        return self._company_names

    @company_names.setter
    def company_names(self, company_names):
        """Sets the company_names of this MFTEntitiesListNames.


        :param company_names: The company_names of this MFTEntitiesListNames.  # noqa: E501
        :type: list[str]
        """

        self._company_names = company_names

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
        if issubclass(MFTEntitiesListNames, dict):
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
        if not isinstance(other, MFTEntitiesListNames):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MFTEntitiesListNames):
            return True

        return self.to_dict() != other.to_dict()
