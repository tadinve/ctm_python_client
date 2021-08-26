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


class RoleDataFull(object):
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
        'overwrite': 'bool',
        'organization_groups': 'list[str]',
        'role_data': 'RoleData'
    }

    attribute_map = {
        'overwrite': 'Overwrite',
        'organization_groups': 'OrganizationGroups',
        'role_data': 'RoleData'
    }

    def __init__(self, overwrite=None, organization_groups=None, role_data=None, _configuration=None):  # noqa: E501
        """RoleDataFull - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._overwrite = None
        self._organization_groups = None
        self._role_data = None
        self.discriminator = None

        if overwrite is not None:
            self.overwrite = overwrite
        if organization_groups is not None:
            self.organization_groups = organization_groups
        if role_data is not None:
            self.role_data = role_data

    @property
    def overwrite(self):
        """Gets the overwrite of this RoleDataFull.  # noqa: E501

        can overwrtie existing role  # noqa: E501

        :return: The overwrite of this RoleDataFull.  # noqa: E501
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this RoleDataFull.

        can overwrtie existing role  # noqa: E501

        :param overwrite: The overwrite of this RoleDataFull.  # noqa: E501
        :type: bool
        """

        self._overwrite = overwrite

    @property
    def organization_groups(self):
        """Gets the organization_groups of this RoleDataFull.  # noqa: E501

        organization groups  # noqa: E501

        :return: The organization_groups of this RoleDataFull.  # noqa: E501
        :rtype: list[str]
        """
        return self._organization_groups

    @organization_groups.setter
    def organization_groups(self, organization_groups):
        """Sets the organization_groups of this RoleDataFull.

        organization groups  # noqa: E501

        :param organization_groups: The organization_groups of this RoleDataFull.  # noqa: E501
        :type: list[str]
        """

        self._organization_groups = organization_groups

    @property
    def role_data(self):
        """Gets the role_data of this RoleDataFull.  # noqa: E501

        authorization role  # noqa: E501

        :return: The role_data of this RoleDataFull.  # noqa: E501
        :rtype: RoleData
        """
        return self._role_data

    @role_data.setter
    def role_data(self, role_data):
        """Sets the role_data of this RoleDataFull.

        authorization role  # noqa: E501

        :param role_data: The role_data of this RoleDataFull.  # noqa: E501
        :type: RoleData
        """

        self._role_data = role_data

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
        if issubclass(RoleDataFull, dict):
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
        if not isinstance(other, RoleDataFull):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleDataFull):
            return True

        return self.to_dict() != other.to_dict()
