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


class ComponentKeyWithStatusType(object):
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
        'component_key': 'ComponentMftKeyType',
        'status': 'int'
    }

    attribute_map = {
        'component_key': 'componentKey',
        'status': 'status'
    }

    def __init__(self, component_key=None, status=None, _configuration=None):  # noqa: E501
        """ComponentKeyWithStatusType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._component_key = None
        self._status = None
        self.discriminator = None

        if component_key is not None:
            self.component_key = component_key
        if status is not None:
            self.status = status

    @property
    def component_key(self):
        """Gets the component_key of this ComponentKeyWithStatusType.  # noqa: E501

        MFT component details  # noqa: E501

        :return: The component_key of this ComponentKeyWithStatusType.  # noqa: E501
        :rtype: ComponentMftKeyType
        """
        return self._component_key

    @component_key.setter
    def component_key(self, component_key):
        """Sets the component_key of this ComponentKeyWithStatusType.

        MFT component details  # noqa: E501

        :param component_key: The component_key of this ComponentKeyWithStatusType.  # noqa: E501
        :type: ComponentMftKeyType
        """

        self._component_key = component_key

    @property
    def status(self):
        """Gets the status of this ComponentKeyWithStatusType.  # noqa: E501

        Component status  # noqa: E501

        :return: The status of this ComponentKeyWithStatusType.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComponentKeyWithStatusType.

        Component status  # noqa: E501

        :param status: The status of this ComponentKeyWithStatusType.  # noqa: E501
        :type: int
        """

        self._status = status

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
        if issubclass(ComponentKeyWithStatusType, dict):
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
        if not isinstance(other, ComponentKeyWithStatusType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentKeyWithStatusType):
            return True

        return self.to_dict() != other.to_dict()
