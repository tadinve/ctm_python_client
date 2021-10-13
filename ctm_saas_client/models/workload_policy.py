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


class WorkloadPolicy(object):
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
        'state': 'str',
        'order_no': 'str',
        'last_update': 'str',
        'updated_by': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'state': 'state',
        'order_no': 'orderNo',
        'last_update': 'lastUpdate',
        'updated_by': 'updatedBy',
        'description': 'description'
    }

    def __init__(self, name=None, state=None, order_no=None, last_update=None, updated_by=None, description=None, _configuration=None):  # noqa: E501
        """WorkloadPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._state = None
        self._order_no = None
        self._last_update = None
        self._updated_by = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if order_no is not None:
            self.order_no = order_no
        if last_update is not None:
            self.last_update = last_update
        if updated_by is not None:
            self.updated_by = updated_by
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this WorkloadPolicy.  # noqa: E501

        unique workload policy name  # noqa: E501

        :return: The name of this WorkloadPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkloadPolicy.

        unique workload policy name  # noqa: E501

        :param name: The name of this WorkloadPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this WorkloadPolicy.  # noqa: E501

        workload policy state  # noqa: E501

        :return: The state of this WorkloadPolicy.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WorkloadPolicy.

        workload policy state  # noqa: E501

        :param state: The state of this WorkloadPolicy.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def order_no(self):
        """Gets the order_no of this WorkloadPolicy.  # noqa: E501

        workload policy order number  # noqa: E501

        :return: The order_no of this WorkloadPolicy.  # noqa: E501
        :rtype: str
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this WorkloadPolicy.

        workload policy order number  # noqa: E501

        :param order_no: The order_no of this WorkloadPolicy.  # noqa: E501
        :type: str
        """

        self._order_no = order_no

    @property
    def last_update(self):
        """Gets the last_update of this WorkloadPolicy.  # noqa: E501

        workload policy update date  # noqa: E501

        :return: The last_update of this WorkloadPolicy.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this WorkloadPolicy.

        workload policy update date  # noqa: E501

        :param last_update: The last_update of this WorkloadPolicy.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def updated_by(self):
        """Gets the updated_by of this WorkloadPolicy.  # noqa: E501

        user which updated workload policy  # noqa: E501

        :return: The updated_by of this WorkloadPolicy.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this WorkloadPolicy.

        user which updated workload policy  # noqa: E501

        :param updated_by: The updated_by of this WorkloadPolicy.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def description(self):
        """Gets the description of this WorkloadPolicy.  # noqa: E501

        workload policy description  # noqa: E501

        :return: The description of this WorkloadPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkloadPolicy.

        workload policy description  # noqa: E501

        :param description: The description of this WorkloadPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(WorkloadPolicy, dict):
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
        if not isinstance(other, WorkloadPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkloadPolicy):
            return True

        return self.to_dict() != other.to_dict()
