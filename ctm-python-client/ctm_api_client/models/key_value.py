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


class KeyValue(object):
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
        'value': 'str',
        'default_value': 'str',
        'validation': 'str',
        'category': 'str',
        'description': 'str',
        'err_msg': 'str',
        'verification': 'str',
        'table': 'str',
        'type': 'str',
        'limits': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'default_value': 'defaultValue',
        'validation': 'validation',
        'category': 'category',
        'description': 'description',
        'err_msg': 'errMsg',
        'verification': 'verification',
        'table': 'table',
        'type': 'type',
        'limits': 'limits'
    }

    def __init__(self, name=None, value=None, default_value=None, validation=None, category=None, description=None, err_msg=None, verification=None, table=None, type=None, limits=None, _configuration=None):  # noqa: E501
        """KeyValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._value = None
        self._default_value = None
        self._validation = None
        self._category = None
        self._description = None
        self._err_msg = None
        self._verification = None
        self._table = None
        self._type = None
        self._limits = None
        self.discriminator = None

        self.name = name
        self.value = value
        if default_value is not None:
            self.default_value = default_value
        if validation is not None:
            self.validation = validation
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if err_msg is not None:
            self.err_msg = err_msg
        if verification is not None:
            self.verification = verification
        if table is not None:
            self.table = table
        if type is not None:
            self.type = type
        if limits is not None:
            self.limits = limits

    @property
    def name(self):
        """Gets the name of this KeyValue.  # noqa: E501

        Unique key  # noqa: E501

        :return: The name of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeyValue.

        Unique key  # noqa: E501

        :param name: The name of this KeyValue.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this KeyValue.  # noqa: E501

        Any value in string form.  # noqa: E501

        :return: The value of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this KeyValue.

        Any value in string form.  # noqa: E501

        :param value: The value of this KeyValue.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def default_value(self):
        """Gets the default_value of this KeyValue.  # noqa: E501

        The default value if exist.  # noqa: E501

        :return: The default_value of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this KeyValue.

        The default value if exist.  # noqa: E501

        :param default_value: The default_value of this KeyValue.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def validation(self):
        """Gets the validation of this KeyValue.  # noqa: E501

        The validation type number.  # noqa: E501

        :return: The validation of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this KeyValue.

        The validation type number.  # noqa: E501

        :param validation: The validation of this KeyValue.  # noqa: E501
        :type: str
        """

        self._validation = validation

    @property
    def category(self):
        """Gets the category of this KeyValue.  # noqa: E501

        The category of the parameter.  # noqa: E501

        :return: The category of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this KeyValue.

        The category of the parameter.  # noqa: E501

        :param category: The category of this KeyValue.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this KeyValue.  # noqa: E501

        The description of the parameter.  # noqa: E501

        :return: The description of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeyValue.

        The description of the parameter.  # noqa: E501

        :param description: The description of this KeyValue.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def err_msg(self):
        """Gets the err_msg of this KeyValue.  # noqa: E501

        The error message of the parameter.  # noqa: E501

        :return: The err_msg of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._err_msg

    @err_msg.setter
    def err_msg(self, err_msg):
        """Sets the err_msg of this KeyValue.

        The error message of the parameter.  # noqa: E501

        :param err_msg: The err_msg of this KeyValue.  # noqa: E501
        :type: str
        """

        self._err_msg = err_msg

    @property
    def verification(self):
        """Gets the verification of this KeyValue.  # noqa: E501

        The verification type of the parameter.  # noqa: E501

        :return: The verification of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        """Sets the verification of this KeyValue.

        The verification type of the parameter.  # noqa: E501

        :param verification: The verification of this KeyValue.  # noqa: E501
        :type: str
        """

        self._verification = verification

    @property
    def table(self):
        """Gets the table of this KeyValue.  # noqa: E501

        The table the parameter belongs to.  # noqa: E501

        :return: The table of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this KeyValue.

        The table the parameter belongs to.  # noqa: E501

        :param table: The table of this KeyValue.  # noqa: E501
        :type: str
        """

        self._table = table

    @property
    def type(self):
        """Gets the type of this KeyValue.  # noqa: E501

        The parameter type.  # noqa: E501

        :return: The type of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this KeyValue.

        The parameter type.  # noqa: E501

        :param type: The type of this KeyValue.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def limits(self):
        """Gets the limits of this KeyValue.  # noqa: E501

        The validation limits of the parameter.  # noqa: E501

        :return: The limits of this KeyValue.  # noqa: E501
        :rtype: str
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this KeyValue.

        The validation limits of the parameter.  # noqa: E501

        :param limits: The limits of this KeyValue.  # noqa: E501
        :type: str
        """

        self._limits = limits

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
        if issubclass(KeyValue, dict):
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
        if not isinstance(other, KeyValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeyValue):
            return True

        return self.to_dict() != other.to_dict()
