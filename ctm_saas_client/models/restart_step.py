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


class RestartStep(object):
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
        'pgm': 'str',
        'proc': 'str'
    }

    attribute_map = {
        'pgm': 'pgm',
        'proc': 'proc'
    }

    def __init__(self, pgm=None, proc=None, _configuration=None):  # noqa: E501
        """RestartStep - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pgm = None
        self._proc = None
        self.discriminator = None

        if pgm is not None:
            self.pgm = pgm
        if proc is not None:
            self.proc = proc

    @property
    def pgm(self):
        """Gets the pgm of this RestartStep.  # noqa: E501

        program step  # noqa: E501

        :return: The pgm of this RestartStep.  # noqa: E501
        :rtype: str
        """
        return self._pgm

    @pgm.setter
    def pgm(self, pgm):
        """Sets the pgm of this RestartStep.

        program step  # noqa: E501

        :param pgm: The pgm of this RestartStep.  # noqa: E501
        :type: str
        """

        self._pgm = pgm

    @property
    def proc(self):
        """Gets the proc of this RestartStep.  # noqa: E501

        proc step  # noqa: E501

        :return: The proc of this RestartStep.  # noqa: E501
        :rtype: str
        """
        return self._proc

    @proc.setter
    def proc(self, proc):
        """Sets the proc of this RestartStep.

        proc step  # noqa: E501

        :param proc: The proc of this RestartStep.  # noqa: E501
        :type: str
        """

        self._proc = proc

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
        if issubclass(RestartStep, dict):
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
        if not isinstance(other, RestartStep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RestartStep):
            return True

        return self.to_dict() != other.to_dict()
