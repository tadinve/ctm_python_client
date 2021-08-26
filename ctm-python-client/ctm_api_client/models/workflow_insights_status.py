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


class WorkflowInsightsStatus(object):
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
        'topology': 'list[Topology]',
        'system_parameters': 'list[SystemParameter]'
    }

    attribute_map = {
        'topology': 'topology',
        'system_parameters': 'systemParameters'
    }

    def __init__(self, topology=None, system_parameters=None, _configuration=None):  # noqa: E501
        """WorkflowInsightsStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._topology = None
        self._system_parameters = None
        self.discriminator = None

        if topology is not None:
            self.topology = topology
        if system_parameters is not None:
            self.system_parameters = system_parameters

    @property
    def topology(self):
        """Gets the topology of this WorkflowInsightsStatus.  # noqa: E501


        :return: The topology of this WorkflowInsightsStatus.  # noqa: E501
        :rtype: list[Topology]
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """Sets the topology of this WorkflowInsightsStatus.


        :param topology: The topology of this WorkflowInsightsStatus.  # noqa: E501
        :type: list[Topology]
        """

        self._topology = topology

    @property
    def system_parameters(self):
        """Gets the system_parameters of this WorkflowInsightsStatus.  # noqa: E501


        :return: The system_parameters of this WorkflowInsightsStatus.  # noqa: E501
        :rtype: list[SystemParameter]
        """
        return self._system_parameters

    @system_parameters.setter
    def system_parameters(self, system_parameters):
        """Sets the system_parameters of this WorkflowInsightsStatus.


        :param system_parameters: The system_parameters of this WorkflowInsightsStatus.  # noqa: E501
        :type: list[SystemParameter]
        """

        self._system_parameters = system_parameters

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
        if issubclass(WorkflowInsightsStatus, dict):
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
        if not isinstance(other, WorkflowInsightsStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowInsightsStatus):
            return True

        return self.to_dict() != other.to_dict()
