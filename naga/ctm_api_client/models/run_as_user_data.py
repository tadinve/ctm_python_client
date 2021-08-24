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


class RunAsUserData(object):
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
        'agent': 'str',
        'user': 'str',
        'password': 'str',
        'key': 'RunAsUserKeyData'
    }

    attribute_map = {
        'agent': 'agent',
        'user': 'user',
        'password': 'password',
        'key': 'key'
    }

    def __init__(self, agent=None, user=None, password=None, key=None, _configuration=None):  # noqa: E501
        """RunAsUserData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent = None
        self._user = None
        self._password = None
        self._key = None
        self.discriminator = None

        if agent is not None:
            self.agent = agent
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password
        if key is not None:
            self.key = key

    @property
    def agent(self):
        """Gets the agent of this RunAsUserData.  # noqa: E501

        agent name, can ended by wildcard REQUIRED  # noqa: E501

        :return: The agent of this RunAsUserData.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this RunAsUserData.

        agent name, can ended by wildcard REQUIRED  # noqa: E501

        :param agent: The agent of this RunAsUserData.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def user(self):
        """Gets the user of this RunAsUserData.  # noqa: E501

        user name REQUIRED  # noqa: E501

        :return: The user of this RunAsUserData.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RunAsUserData.

        user name REQUIRED  # noqa: E501

        :param user: The user of this RunAsUserData.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def password(self):
        """Gets the password of this RunAsUserData.  # noqa: E501

        Password  # noqa: E501

        :return: The password of this RunAsUserData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RunAsUserData.

        Password  # noqa: E501

        :param password: The password of this RunAsUserData.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def key(self):
        """Gets the key of this RunAsUserData.  # noqa: E501

        HIDDEN  # noqa: E501

        :return: The key of this RunAsUserData.  # noqa: E501
        :rtype: RunAsUserKeyData
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RunAsUserData.

        HIDDEN  # noqa: E501

        :param key: The key of this RunAsUserData.  # noqa: E501
        :type: RunAsUserKeyData
        """

        self._key = key

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
        if issubclass(RunAsUserData, dict):
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
        if not isinstance(other, RunAsUserData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunAsUserData):
            return True

        return self.to_dict() != other.to_dict()
