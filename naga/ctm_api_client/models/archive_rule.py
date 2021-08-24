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


class ArchiveRule(object):
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
        'name': 'str',
        'description': 'str',
        'max_output_size': 'str',
        'max_output_size_type': 'str',
        'trim_type': 'str',
        'retention': 'str',
        'retention_type': 'str',
        'is_active': 'str',
        'archived_type': 'str',
        'rule_parameters': 'list[RuleCriteria]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'max_output_size': 'maxOutputSize',
        'max_output_size_type': 'maxOutputSizeType',
        'trim_type': 'trimType',
        'retention': 'retention',
        'retention_type': 'retentionType',
        'is_active': 'isActive',
        'archived_type': 'archivedType',
        'rule_parameters': 'ruleParameters'
    }

    def __init__(self, name=None, description=None, max_output_size=None, max_output_size_type=None, trim_type=None, retention=None, retention_type=None, is_active=None, archived_type=None, rule_parameters=None, _configuration=None):  # noqa: E501
        """ArchiveRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._max_output_size = None
        self._max_output_size_type = None
        self._trim_type = None
        self._retention = None
        self._retention_type = None
        self._is_active = None
        self._archived_type = None
        self._rule_parameters = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if max_output_size is not None:
            self.max_output_size = max_output_size
        if max_output_size_type is not None:
            self.max_output_size_type = max_output_size_type
        if trim_type is not None:
            self.trim_type = trim_type
        if retention is not None:
            self.retention = retention
        if retention_type is not None:
            self.retention_type = retention_type
        if is_active is not None:
            self.is_active = is_active
        if archived_type is not None:
            self.archived_type = archived_type
        if rule_parameters is not None:
            self.rule_parameters = rule_parameters

    @property
    def name(self):
        """Gets the name of this ArchiveRule.  # noqa: E501

        The Control-M Workload Archiving rule name. REQUIRED. HIDDEN.  # noqa: E501

        :return: The name of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArchiveRule.

        The Control-M Workload Archiving rule name. REQUIRED. HIDDEN.  # noqa: E501

        :param name: The name of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ArchiveRule.  # noqa: E501

        The description of Control-M Workload Archiving rule. HIDDEN.  # noqa: E501

        :return: The description of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ArchiveRule.

        The description of Control-M Workload Archiving rule. HIDDEN.  # noqa: E501

        :param description: The description of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def max_output_size(self):
        """Gets the max_output_size of this ArchiveRule.  # noqa: E501

        The maximum job's output size to collect. HIDDEN.  # noqa: E501

        :return: The max_output_size of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._max_output_size

    @max_output_size.setter
    def max_output_size(self, max_output_size):
        """Sets the max_output_size of this ArchiveRule.

        The maximum job's output size to collect. HIDDEN.  # noqa: E501

        :param max_output_size: The max_output_size of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._max_output_size = max_output_size

    @property
    def max_output_size_type(self):
        """Gets the max_output_size_type of this ArchiveRule.  # noqa: E501

        The maximum job's output size type to collect - KB or MB. The default is MB. HIDDEN.  # noqa: E501

        :return: The max_output_size_type of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._max_output_size_type

    @max_output_size_type.setter
    def max_output_size_type(self, max_output_size_type):
        """Sets the max_output_size_type of this ArchiveRule.

        The maximum job's output size type to collect - KB or MB. The default is MB. HIDDEN.  # noqa: E501

        :param max_output_size_type: The max_output_size_type of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._max_output_size_type = max_output_size_type

    @property
    def trim_type(self):
        """Gets the trim_type of this ArchiveRule.  # noqa: E501

        Trim in case the output exceed the maximum job's output - Omit , Beginning, End. The default is to Omit. HIDDEN.  # noqa: E501

        :return: The trim_type of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._trim_type

    @trim_type.setter
    def trim_type(self, trim_type):
        """Sets the trim_type of this ArchiveRule.

        Trim in case the output exceed the maximum job's output - Omit , Beginning, End. The default is to Omit. HIDDEN.  # noqa: E501

        :param trim_type: The trim_type of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._trim_type = trim_type

    @property
    def retention(self):
        """Gets the retention of this ArchiveRule.  # noqa: E501

        The retention period to keep archive job by rule. The default is 1. HIDDEN.  # noqa: E501

        :return: The retention of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this ArchiveRule.

        The retention period to keep archive job by rule. The default is 1. HIDDEN.  # noqa: E501

        :param retention: The retention of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._retention = retention

    @property
    def retention_type(self):
        """Gets the retention_type of this ArchiveRule.  # noqa: E501

        The retention period type to keep archive job by rule- Years, Months and Days are available. The default is Years. HIDDEN.  # noqa: E501

        :return: The retention_type of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._retention_type

    @retention_type.setter
    def retention_type(self, retention_type):
        """Sets the retention_type of this ArchiveRule.

        The retention period type to keep archive job by rule- Years, Months and Days are available. The default is Years. HIDDEN.  # noqa: E501

        :param retention_type: The retention_type of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._retention_type = retention_type

    @property
    def is_active(self):
        """Gets the is_active of this ArchiveRule.  # noqa: E501

        Is Control-M Workload Archiving rule is active. HIDDEN.  # noqa: E501

        :return: The is_active of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ArchiveRule.

        Is Control-M Workload Archiving rule is active. HIDDEN.  # noqa: E501

        :param is_active: The is_active of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._is_active = is_active

    @property
    def archived_type(self):
        """Gets the archived_type of this ArchiveRule.  # noqa: E501

        The rule archived data - logs, output or both. The default is both. HIDDEN.  # noqa: E501

        :return: The archived_type of this ArchiveRule.  # noqa: E501
        :rtype: str
        """
        return self._archived_type

    @archived_type.setter
    def archived_type(self, archived_type):
        """Sets the archived_type of this ArchiveRule.

        The rule archived data - logs, output or both. The default is both. HIDDEN.  # noqa: E501

        :param archived_type: The archived_type of this ArchiveRule.  # noqa: E501
        :type: str
        """

        self._archived_type = archived_type

    @property
    def rule_parameters(self):
        """Gets the rule_parameters of this ArchiveRule.  # noqa: E501

        Rule parameters - ctm, type, jobName, jobType, application, subApplication, jobStatus, folder and library. HIDDEN.  # noqa: E501

        :return: The rule_parameters of this ArchiveRule.  # noqa: E501
        :rtype: list[RuleCriteria]
        """
        return self._rule_parameters

    @rule_parameters.setter
    def rule_parameters(self, rule_parameters):
        """Sets the rule_parameters of this ArchiveRule.

        Rule parameters - ctm, type, jobName, jobType, application, subApplication, jobStatus, folder and library. HIDDEN.  # noqa: E501

        :param rule_parameters: The rule_parameters of this ArchiveRule.  # noqa: E501
        :type: list[RuleCriteria]
        """

        self._rule_parameters = rule_parameters

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
        if issubclass(ArchiveRule, dict):
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
        if not isinstance(other, ArchiveRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArchiveRule):
            return True

        return self.to_dict() != other.to_dict()
