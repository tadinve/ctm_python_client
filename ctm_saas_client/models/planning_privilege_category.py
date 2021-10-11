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


class PlanningPrivilegeCategory(object):
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
        'periodical_statistics': 'str',
        'forecast_or_batch_impact_manager_config': 'str',
        'promotion_rules': 'str',
        'promote_action': 'str'
    }

    attribute_map = {
        'periodical_statistics': 'PeriodicalStatistics',
        'forecast_or_batch_impact_manager_config': 'ForecastOrBatchImpactManagerConfig',
        'promotion_rules': 'PromotionRules',
        'promote_action': 'PromoteAction'
    }

    def __init__(self, periodical_statistics=None, forecast_or_batch_impact_manager_config=None, promotion_rules=None, promote_action=None, _configuration=None):  # noqa: E501
        """PlanningPrivilegeCategory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._periodical_statistics = None
        self._forecast_or_batch_impact_manager_config = None
        self._promotion_rules = None
        self._promote_action = None
        self.discriminator = None

        if periodical_statistics is not None:
            self.periodical_statistics = periodical_statistics
        if forecast_or_batch_impact_manager_config is not None:
            self.forecast_or_batch_impact_manager_config = forecast_or_batch_impact_manager_config
        if promotion_rules is not None:
            self.promotion_rules = promotion_rules
        if promote_action is not None:
            self.promote_action = promote_action

    @property
    def periodical_statistics(self):
        """Gets the periodical_statistics of this PlanningPrivilegeCategory.  # noqa: E501

        Periodical Statistics access level (None, Browse, Update, Full)  # noqa: E501

        :return: The periodical_statistics of this PlanningPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._periodical_statistics

    @periodical_statistics.setter
    def periodical_statistics(self, periodical_statistics):
        """Sets the periodical_statistics of this PlanningPrivilegeCategory.

        Periodical Statistics access level (None, Browse, Update, Full)  # noqa: E501

        :param periodical_statistics: The periodical_statistics of this PlanningPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._periodical_statistics = periodical_statistics

    @property
    def forecast_or_batch_impact_manager_config(self):
        """Gets the forecast_or_batch_impact_manager_config of this PlanningPrivilegeCategory.  # noqa: E501

        Forecast/BIM Configuration access level (None, Browse, Update, Full)  # noqa: E501

        :return: The forecast_or_batch_impact_manager_config of this PlanningPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._forecast_or_batch_impact_manager_config

    @forecast_or_batch_impact_manager_config.setter
    def forecast_or_batch_impact_manager_config(self, forecast_or_batch_impact_manager_config):
        """Sets the forecast_or_batch_impact_manager_config of this PlanningPrivilegeCategory.

        Forecast/BIM Configuration access level (None, Browse, Update, Full)  # noqa: E501

        :param forecast_or_batch_impact_manager_config: The forecast_or_batch_impact_manager_config of this PlanningPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._forecast_or_batch_impact_manager_config = forecast_or_batch_impact_manager_config

    @property
    def promotion_rules(self):
        """Gets the promotion_rules of this PlanningPrivilegeCategory.  # noqa: E501

        Promotion Rules access level (None, Browse, Update, Full)  # noqa: E501

        :return: The promotion_rules of this PlanningPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._promotion_rules

    @promotion_rules.setter
    def promotion_rules(self, promotion_rules):
        """Sets the promotion_rules of this PlanningPrivilegeCategory.

        Promotion Rules access level (None, Browse, Update, Full)  # noqa: E501

        :param promotion_rules: The promotion_rules of this PlanningPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._promotion_rules = promotion_rules

    @property
    def promote_action(self):
        """Gets the promote_action of this PlanningPrivilegeCategory.  # noqa: E501

        Promote Action access level (None, Browse, Update, Full)  # noqa: E501

        :return: The promote_action of this PlanningPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._promote_action

    @promote_action.setter
    def promote_action(self, promote_action):
        """Sets the promote_action of this PlanningPrivilegeCategory.

        Promote Action access level (None, Browse, Update, Full)  # noqa: E501

        :param promote_action: The promote_action of this PlanningPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._promote_action = promote_action

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
        if issubclass(PlanningPrivilegeCategory, dict):
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
        if not isinstance(other, PlanningPrivilegeCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlanningPrivilegeCategory):
            return True

        return self.to_dict() != other.to_dict()
