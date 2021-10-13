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


class HostGroupData(object):
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
        'hostgroup': 'str',
        'tag': 'str',
        'agentslist': 'list[AgentInGroupParams]'
    }

    attribute_map = {
        'hostgroup': 'hostgroup',
        'tag': 'tag',
        'agentslist': 'agentslist'
    }

    def __init__(self, hostgroup=None, tag=None, agentslist=None, _configuration=None):  # noqa: E501
        """HostGroupData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hostgroup = None
        self._tag = None
        self._agentslist = None
        self.discriminator = None

        if hostgroup is not None:
            self.hostgroup = hostgroup
        if tag is not None:
            self.tag = tag
        if agentslist is not None:
            self.agentslist = agentslist

    @property
    def hostgroup(self):
        """Gets the hostgroup of this HostGroupData.  # noqa: E501

        Host Group name  # noqa: E501

        :return: The hostgroup of this HostGroupData.  # noqa: E501
        :rtype: str
        """
        return self._hostgroup

    @hostgroup.setter
    def hostgroup(self, hostgroup):
        """Sets the hostgroup of this HostGroupData.

        Host Group name  # noqa: E501

        :param hostgroup: The hostgroup of this HostGroupData.  # noqa: E501
        :type: str
        """

        self._hostgroup = hostgroup

    @property
    def tag(self):
        """Gets the tag of this HostGroupData.  # noqa: E501

        Host Group tag  # noqa: E501

        :return: The tag of this HostGroupData.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this HostGroupData.

        Host Group tag  # noqa: E501

        :param tag: The tag of this HostGroupData.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def agentslist(self):
        """Gets the agentslist of this HostGroupData.  # noqa: E501

        Agents list  # noqa: E501

        :return: The agentslist of this HostGroupData.  # noqa: E501
        :rtype: list[AgentInGroupParams]
        """
        return self._agentslist

    @agentslist.setter
    def agentslist(self, agentslist):
        """Sets the agentslist of this HostGroupData.

        Agents list  # noqa: E501

        :param agentslist: The agentslist of this HostGroupData.  # noqa: E501
        :type: list[AgentInGroupParams]
        """

        self._agentslist = agentslist

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
        if issubclass(HostGroupData, dict):
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
        if not isinstance(other, HostGroupData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostGroupData):
            return True

        return self.to_dict() != other.to_dict()
