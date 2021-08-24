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


class SectionMetadataProperties(object):
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
        'display_name': 'str',
        'display_name1': 'str',
        'display_name_id': 'str',
        'fields': 'list[FieldMetadataProperties]',
        'name': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'display_name1': 'displayName1',
        'display_name_id': 'displayNameID',
        'fields': 'fields',
        'name': 'name'
    }

    def __init__(self, display_name=None, display_name1=None, display_name_id=None, fields=None, name=None, _configuration=None):  # noqa: E501
        """SectionMetadataProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._display_name1 = None
        self._display_name_id = None
        self._fields = None
        self._name = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if display_name1 is not None:
            self.display_name1 = display_name1
        if display_name_id is not None:
            self.display_name_id = display_name_id
        if fields is not None:
            self.fields = fields
        if name is not None:
            self.name = name

    @property
    def display_name(self):
        """Gets the display_name of this SectionMetadataProperties.  # noqa: E501


        :return: The display_name of this SectionMetadataProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SectionMetadataProperties.


        :param display_name: The display_name of this SectionMetadataProperties.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def display_name1(self):
        """Gets the display_name1 of this SectionMetadataProperties.  # noqa: E501


        :return: The display_name1 of this SectionMetadataProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name1

    @display_name1.setter
    def display_name1(self, display_name1):
        """Sets the display_name1 of this SectionMetadataProperties.


        :param display_name1: The display_name1 of this SectionMetadataProperties.  # noqa: E501
        :type: str
        """

        self._display_name1 = display_name1

    @property
    def display_name_id(self):
        """Gets the display_name_id of this SectionMetadataProperties.  # noqa: E501


        :return: The display_name_id of this SectionMetadataProperties.  # noqa: E501
        :rtype: str
        """
        return self._display_name_id

    @display_name_id.setter
    def display_name_id(self, display_name_id):
        """Sets the display_name_id of this SectionMetadataProperties.


        :param display_name_id: The display_name_id of this SectionMetadataProperties.  # noqa: E501
        :type: str
        """

        self._display_name_id = display_name_id

    @property
    def fields(self):
        """Gets the fields of this SectionMetadataProperties.  # noqa: E501


        :return: The fields of this SectionMetadataProperties.  # noqa: E501
        :rtype: list[FieldMetadataProperties]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this SectionMetadataProperties.


        :param fields: The fields of this SectionMetadataProperties.  # noqa: E501
        :type: list[FieldMetadataProperties]
        """

        self._fields = fields

    @property
    def name(self):
        """Gets the name of this SectionMetadataProperties.  # noqa: E501


        :return: The name of this SectionMetadataProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SectionMetadataProperties.


        :param name: The name of this SectionMetadataProperties.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(SectionMetadataProperties, dict):
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
        if not isinstance(other, SectionMetadataProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SectionMetadataProperties):
            return True

        return self.to_dict() != other.to_dict()
