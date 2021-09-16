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


class UpgradeAgentInfo(object):
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
        "agent": "str",
        "ctm": "str",
        "type": "str",
        "platform": "str",
        "from_version": "str",
        "to_version": "str",
    }

    attribute_map = {
        "agent": "agent",
        "ctm": "ctm",
        "type": "type",
        "platform": "platform",
        "from_version": "fromVersion",
        "to_version": "toVersion",
    }

    def __init__(
        self,
        agent=None,
        ctm=None,
        type=None,
        platform=None,
        from_version=None,
        to_version=None,
        _configuration=None,
    ):  # noqa: E501
        """UpgradeAgentInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent = None
        self._ctm = None
        self._type = None
        self._platform = None
        self._from_version = None
        self._to_version = None
        self.discriminator = None

        if agent is not None:
            self.agent = agent
        if ctm is not None:
            self.ctm = ctm
        if type is not None:
            self.type = type
        if platform is not None:
            self.platform = platform
        if from_version is not None:
            self.from_version = from_version
        if to_version is not None:
            self.to_version = to_version

    @property
    def agent(self):
        """Gets the agent of this UpgradeAgentInfo.  # noqa: E501

        Agent name.  # noqa: E501

        :return: The agent of this UpgradeAgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this UpgradeAgentInfo.

        Agent name.  # noqa: E501

        :param agent: The agent of this UpgradeAgentInfo.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def ctm(self):
        """Gets the ctm of this UpgradeAgentInfo.  # noqa: E501

        Control-M name.  # noqa: E501

        :return: The ctm of this UpgradeAgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this UpgradeAgentInfo.

        Control-M name.  # noqa: E501

        :param ctm: The ctm of this UpgradeAgentInfo.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def type(self):
        """Gets the type of this UpgradeAgentInfo.  # noqa: E501

        Agent type (Agent, MFT, AppPack).  # noqa: E501

        :return: The type of this UpgradeAgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpgradeAgentInfo.

        Agent type (Agent, MFT, AppPack).  # noqa: E501

        :param type: The type of this UpgradeAgentInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def platform(self):
        """Gets the platform of this UpgradeAgentInfo.  # noqa: E501

        Platform.  # noqa: E501

        :return: The platform of this UpgradeAgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this UpgradeAgentInfo.

        Platform.  # noqa: E501

        :param platform: The platform of this UpgradeAgentInfo.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def from_version(self):
        """Gets the from_version of this UpgradeAgentInfo.  # noqa: E501

        From version.  # noqa: E501

        :return: The from_version of this UpgradeAgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._from_version

    @from_version.setter
    def from_version(self, from_version):
        """Sets the from_version of this UpgradeAgentInfo.

        From version.  # noqa: E501

        :param from_version: The from_version of this UpgradeAgentInfo.  # noqa: E501
        :type: str
        """

        self._from_version = from_version

    @property
    def to_version(self):
        """Gets the to_version of this UpgradeAgentInfo.  # noqa: E501

        To version.  # noqa: E501

        :return: The to_version of this UpgradeAgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._to_version

    @to_version.setter
    def to_version(self, to_version):
        """Sets the to_version of this UpgradeAgentInfo.

        To version.  # noqa: E501

        :param to_version: The to_version of this UpgradeAgentInfo.  # noqa: E501
        :type: str
        """

        self._to_version = to_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(UpgradeAgentInfo, dict):
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
        if not isinstance(other, UpgradeAgentInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpgradeAgentInfo):
            return True

        return self.to_dict() != other.to_dict()
