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


class ViewpointManagerPrivilegeCategory(object):
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
        'collections': 'str',
        'hierarchies': 'str',
        'filters': 'str',
        'viewpoints': 'str'
    }

    attribute_map = {
        'collections': 'Collections',
        'hierarchies': 'Hierarchies',
        'filters': 'Filters',
        'viewpoints': 'Viewpoints'
    }

    def __init__(self, collections=None, hierarchies=None, filters=None, viewpoints=None, _configuration=None):  # noqa: E501
        """ViewpointManagerPrivilegeCategory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._collections = None
        self._hierarchies = None
        self._filters = None
        self._viewpoints = None
        self.discriminator = None

        if collections is not None:
            self.collections = collections
        if hierarchies is not None:
            self.hierarchies = hierarchies
        if filters is not None:
            self.filters = filters
        if viewpoints is not None:
            self.viewpoints = viewpoints

    @property
    def collections(self):
        """Gets the collections of this ViewpointManagerPrivilegeCategory.  # noqa: E501

        Collections access level (None, Browse, Update, Full)  # noqa: E501

        :return: The collections of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this ViewpointManagerPrivilegeCategory.

        Collections access level (None, Browse, Update, Full)  # noqa: E501

        :param collections: The collections of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._collections = collections

    @property
    def hierarchies(self):
        """Gets the hierarchies of this ViewpointManagerPrivilegeCategory.  # noqa: E501

        Hierarchies access level (None, Browse, Update, Full)  # noqa: E501

        :return: The hierarchies of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._hierarchies

    @hierarchies.setter
    def hierarchies(self, hierarchies):
        """Sets the hierarchies of this ViewpointManagerPrivilegeCategory.

        Hierarchies access level (None, Browse, Update, Full)  # noqa: E501

        :param hierarchies: The hierarchies of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._hierarchies = hierarchies

    @property
    def filters(self):
        """Gets the filters of this ViewpointManagerPrivilegeCategory.  # noqa: E501

        Filters access level (None, Browse, Update, Full)  # noqa: E501

        :return: The filters of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ViewpointManagerPrivilegeCategory.

        Filters access level (None, Browse, Update, Full)  # noqa: E501

        :param filters: The filters of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._filters = filters

    @property
    def viewpoints(self):
        """Gets the viewpoints of this ViewpointManagerPrivilegeCategory.  # noqa: E501

        Viewpoints access level (None, Browse, Update, Full)  # noqa: E501

        :return: The viewpoints of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._viewpoints

    @viewpoints.setter
    def viewpoints(self, viewpoints):
        """Sets the viewpoints of this ViewpointManagerPrivilegeCategory.

        Viewpoints access level (None, Browse, Update, Full)  # noqa: E501

        :param viewpoints: The viewpoints of this ViewpointManagerPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._viewpoints = viewpoints

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
        if issubclass(ViewpointManagerPrivilegeCategory, dict):
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
        if not isinstance(other, ViewpointManagerPrivilegeCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ViewpointManagerPrivilegeCategory):
            return True

        return self.to_dict() != other.to_dict()
