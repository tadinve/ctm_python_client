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


class AgentsSysParamSetData(object):
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
        'params_data': 'list[AgentSysParamSetData]'
    }

    attribute_map = {
        'params_data': 'paramsData'
    }

    def __init__(self, params_data=None, _configuration=None):  # noqa: E501
        """AgentsSysParamSetData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._params_data = None
        self.discriminator = None

        if params_data is not None:
            self.params_data = params_data

    @property
    def params_data(self):
        """Gets the params_data of this AgentsSysParamSetData.  # noqa: E501

        The list of agent parameters set data.  # noqa: E501

        :return: The params_data of this AgentsSysParamSetData.  # noqa: E501
        :rtype: list[AgentSysParamSetData]
        """
        return self._params_data

    @params_data.setter
    def params_data(self, params_data):
        """Sets the params_data of this AgentsSysParamSetData.

        The list of agent parameters set data.  # noqa: E501

        :param params_data: The params_data of this AgentsSysParamSetData.  # noqa: E501
        :type: list[AgentSysParamSetData]
        """

        self._params_data = params_data

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
        if issubclass(AgentsSysParamSetData, dict):
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
        if not isinstance(other, AgentsSysParamSetData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentsSysParamSetData):
            return True

        return self.to_dict() != other.to_dict()
