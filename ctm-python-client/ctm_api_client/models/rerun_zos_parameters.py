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


class RerunZosParameters(object):
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
        '_from': 'RestartStep',
        'to': 'RestartStep',
        'cleanup': 'bool',
        'recapture_abend': 'str',
        'recapture_condition_code': 'str',
        'step_adjustment': 'bool',
        'restart_parm_member_name': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'cleanup': 'cleanup',
        'recapture_abend': 'recaptureAbend',
        'recapture_condition_code': 'recaptureConditionCode',
        'step_adjustment': 'stepAdjustment',
        'restart_parm_member_name': 'restartParmMemberName'
    }

    def __init__(self, _from=None, to=None, cleanup=None, recapture_abend=None, recapture_condition_code=None, step_adjustment=None, restart_parm_member_name=None, _configuration=None):  # noqa: E501
        """RerunZosParameters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__from = None
        self._to = None
        self._cleanup = None
        self._recapture_abend = None
        self._recapture_condition_code = None
        self._step_adjustment = None
        self._restart_parm_member_name = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if cleanup is not None:
            self.cleanup = cleanup
        if recapture_abend is not None:
            self.recapture_abend = recapture_abend
        if recapture_condition_code is not None:
            self.recapture_condition_code = recapture_condition_code
        if step_adjustment is not None:
            self.step_adjustment = step_adjustment
        if restart_parm_member_name is not None:
            self.restart_parm_member_name = restart_parm_member_name

    @property
    def _from(self):
        """Gets the _from of this RerunZosParameters.  # noqa: E501

        start from specific step. HIDDEN.  # noqa: E501

        :return: The _from of this RerunZosParameters.  # noqa: E501
        :rtype: RestartStep
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this RerunZosParameters.

        start from specific step. HIDDEN.  # noqa: E501

        :param _from: The _from of this RerunZosParameters.  # noqa: E501
        :type: RestartStep
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this RerunZosParameters.  # noqa: E501

        end at specific step. HIDDEN.  # noqa: E501

        :return: The to of this RerunZosParameters.  # noqa: E501
        :rtype: RestartStep
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this RerunZosParameters.

        end at specific step. HIDDEN.  # noqa: E501

        :param to: The to of this RerunZosParameters.  # noqa: E501
        :type: RestartStep
        """

        self._to = to

    @property
    def cleanup(self):
        """Gets the cleanup of this RerunZosParameters.  # noqa: E501

        cleanup instead of running specific steps. HIDDEN.  # noqa: E501

        :return: The cleanup of this RerunZosParameters.  # noqa: E501
        :rtype: bool
        """
        return self._cleanup

    @cleanup.setter
    def cleanup(self, cleanup):
        """Sets the cleanup of this RerunZosParameters.

        cleanup instead of running specific steps. HIDDEN.  # noqa: E501

        :param cleanup: The cleanup of this RerunZosParameters.  # noqa: E501
        :type: bool
        """

        self._cleanup = cleanup

    @property
    def recapture_abend(self):
        """Gets the recapture_abend of this RerunZosParameters.  # noqa: E501

        TO BE ADDED. HIDDEN.  # noqa: E501

        :return: The recapture_abend of this RerunZosParameters.  # noqa: E501
        :rtype: str
        """
        return self._recapture_abend

    @recapture_abend.setter
    def recapture_abend(self, recapture_abend):
        """Sets the recapture_abend of this RerunZosParameters.

        TO BE ADDED. HIDDEN.  # noqa: E501

        :param recapture_abend: The recapture_abend of this RerunZosParameters.  # noqa: E501
        :type: str
        """

        self._recapture_abend = recapture_abend

    @property
    def recapture_condition_code(self):
        """Gets the recapture_condition_code of this RerunZosParameters.  # noqa: E501

        TO BE ADDED. HIDDEN.  # noqa: E501

        :return: The recapture_condition_code of this RerunZosParameters.  # noqa: E501
        :rtype: str
        """
        return self._recapture_condition_code

    @recapture_condition_code.setter
    def recapture_condition_code(self, recapture_condition_code):
        """Sets the recapture_condition_code of this RerunZosParameters.

        TO BE ADDED. HIDDEN.  # noqa: E501

        :param recapture_condition_code: The recapture_condition_code of this RerunZosParameters.  # noqa: E501
        :type: str
        """

        self._recapture_condition_code = recapture_condition_code

    @property
    def step_adjustment(self):
        """Gets the step_adjustment of this RerunZosParameters.  # noqa: E501

        TO BE ADDED. HIDDEN.  # noqa: E501

        :return: The step_adjustment of this RerunZosParameters.  # noqa: E501
        :rtype: bool
        """
        return self._step_adjustment

    @step_adjustment.setter
    def step_adjustment(self, step_adjustment):
        """Sets the step_adjustment of this RerunZosParameters.

        TO BE ADDED. HIDDEN.  # noqa: E501

        :param step_adjustment: The step_adjustment of this RerunZosParameters.  # noqa: E501
        :type: bool
        """

        self._step_adjustment = step_adjustment

    @property
    def restart_parm_member_name(self):
        """Gets the restart_parm_member_name of this RerunZosParameters.  # noqa: E501

        TO BE ADDED. HIDDEN.  # noqa: E501

        :return: The restart_parm_member_name of this RerunZosParameters.  # noqa: E501
        :rtype: str
        """
        return self._restart_parm_member_name

    @restart_parm_member_name.setter
    def restart_parm_member_name(self, restart_parm_member_name):
        """Sets the restart_parm_member_name of this RerunZosParameters.

        TO BE ADDED. HIDDEN.  # noqa: E501

        :param restart_parm_member_name: The restart_parm_member_name of this RerunZosParameters.  # noqa: E501
        :type: str
        """

        self._restart_parm_member_name = restart_parm_member_name

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
        if issubclass(RerunZosParameters, dict):
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
        if not isinstance(other, RerunZosParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RerunZosParameters):
            return True

        return self.to_dict() != other.to_dict()
