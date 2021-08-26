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

from ctm-python-client.ctm_api_client.configuration import Configuration


class WorkloadPoliciesFileResults(object):
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
        'work_load_policies_file': 'str',
        'success_workpolicies_count': 'int',
        'is_deploy_descriptor_valid': 'bool',
        'added_workload_policies': 'list[str]',
        'errors': 'list[str]'
    }

    attribute_map = {
        'work_load_policies_file': 'workLoadPoliciesFile',
        'success_workpolicies_count': 'successWorkpoliciesCount',
        'is_deploy_descriptor_valid': 'isDeployDescriptorValid',
        'added_workload_policies': 'addedWorkloadPolicies',
        'errors': 'errors'
    }

    def __init__(self, work_load_policies_file=None, success_workpolicies_count=None, is_deploy_descriptor_valid=None, added_workload_policies=None, errors=None, _configuration=None):  # noqa: E501
        """WorkloadPoliciesFileResults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._work_load_policies_file = None
        self._success_workpolicies_count = None
        self._is_deploy_descriptor_valid = None
        self._added_workload_policies = None
        self._errors = None
        self.discriminator = None

        if work_load_policies_file is not None:
            self.work_load_policies_file = work_load_policies_file
        if success_workpolicies_count is not None:
            self.success_workpolicies_count = success_workpolicies_count
        if is_deploy_descriptor_valid is not None:
            self.is_deploy_descriptor_valid = is_deploy_descriptor_valid
        if added_workload_policies is not None:
            self.added_workload_policies = added_workload_policies
        if errors is not None:
            self.errors = errors

    @property
    def work_load_policies_file(self):
        """Gets the work_load_policies_file of this WorkloadPoliciesFileResults.  # noqa: E501

        The name of a specific workLoad policies file.  # noqa: E501

        :return: The work_load_policies_file of this WorkloadPoliciesFileResults.  # noqa: E501
        :rtype: str
        """
        return self._work_load_policies_file

    @work_load_policies_file.setter
    def work_load_policies_file(self, work_load_policies_file):
        """Sets the work_load_policies_file of this WorkloadPoliciesFileResults.

        The name of a specific workLoad policies file.  # noqa: E501

        :param work_load_policies_file: The work_load_policies_file of this WorkloadPoliciesFileResults.  # noqa: E501
        :type: str
        """

        self._work_load_policies_file = work_load_policies_file

    @property
    def success_workpolicies_count(self):
        """Gets the success_workpolicies_count of this WorkloadPoliciesFileResults.  # noqa: E501

        Determines the number of successfully added workload policies.  # noqa: E501

        :return: The success_workpolicies_count of this WorkloadPoliciesFileResults.  # noqa: E501
        :rtype: int
        """
        return self._success_workpolicies_count

    @success_workpolicies_count.setter
    def success_workpolicies_count(self, success_workpolicies_count):
        """Sets the success_workpolicies_count of this WorkloadPoliciesFileResults.

        Determines the number of successfully added workload policies.  # noqa: E501

        :param success_workpolicies_count: The success_workpolicies_count of this WorkloadPoliciesFileResults.  # noqa: E501
        :type: int
        """

        self._success_workpolicies_count = success_workpolicies_count

    @property
    def is_deploy_descriptor_valid(self):
        """Gets the is_deploy_descriptor_valid of this WorkloadPoliciesFileResults.  # noqa: E501

        Determines if the workLoad policies file file is a valid deploy descriptor file.  # noqa: E501

        :return: The is_deploy_descriptor_valid of this WorkloadPoliciesFileResults.  # noqa: E501
        :rtype: bool
        """
        return self._is_deploy_descriptor_valid

    @is_deploy_descriptor_valid.setter
    def is_deploy_descriptor_valid(self, is_deploy_descriptor_valid):
        """Sets the is_deploy_descriptor_valid of this WorkloadPoliciesFileResults.

        Determines if the workLoad policies file file is a valid deploy descriptor file.  # noqa: E501

        :param is_deploy_descriptor_valid: The is_deploy_descriptor_valid of this WorkloadPoliciesFileResults.  # noqa: E501
        :type: bool
        """

        self._is_deploy_descriptor_valid = is_deploy_descriptor_valid

    @property
    def added_workload_policies(self):
        """Gets the added_workload_policies of this WorkloadPoliciesFileResults.  # noqa: E501


        :return: The added_workload_policies of this WorkloadPoliciesFileResults.  # noqa: E501
        :rtype: list[str]
        """
        return self._added_workload_policies

    @added_workload_policies.setter
    def added_workload_policies(self, added_workload_policies):
        """Sets the added_workload_policies of this WorkloadPoliciesFileResults.


        :param added_workload_policies: The added_workload_policies of this WorkloadPoliciesFileResults.  # noqa: E501
        :type: list[str]
        """

        self._added_workload_policies = added_workload_policies

    @property
    def errors(self):
        """Gets the errors of this WorkloadPoliciesFileResults.  # noqa: E501


        :return: The errors of this WorkloadPoliciesFileResults.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this WorkloadPoliciesFileResults.


        :param errors: The errors of this WorkloadPoliciesFileResults.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

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
        if issubclass(WorkloadPoliciesFileResults, dict):
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
        if not isinstance(other, WorkloadPoliciesFileResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkloadPoliciesFileResults):
            return True

        return self.to_dict() != other.to_dict()
