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


class RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter(object):
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
        'ctm_parameters': 'WhyJobParameters',
        'em_parameters': 'EMDefaultRequestParameters'
    }

    attribute_map = {
        'ctm_parameters': 'ctm_parameters',
        'em_parameters': 'em_parameters'
    }

    def __init__(self, ctm_parameters=None, em_parameters=None, _configuration=None):  # noqa: E501
        """RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ctm_parameters = None
        self._em_parameters = None
        self.discriminator = None

        if ctm_parameters is not None:
            self.ctm_parameters = ctm_parameters
        if em_parameters is not None:
            self.em_parameters = em_parameters

    @property
    def ctm_parameters(self):
        """Gets the ctm_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.  # noqa: E501


        :return: The ctm_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.  # noqa: E501
        :rtype: WhyJobParameters
        """
        return self._ctm_parameters

    @ctm_parameters.setter
    def ctm_parameters(self, ctm_parameters):
        """Sets the ctm_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.


        :param ctm_parameters: The ctm_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.  # noqa: E501
        :type: WhyJobParameters
        """

        self._ctm_parameters = ctm_parameters

    @property
    def em_parameters(self):
        """Gets the em_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.  # noqa: E501


        :return: The em_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.  # noqa: E501
        :rtype: EMDefaultRequestParameters
        """
        return self._em_parameters

    @em_parameters.setter
    def em_parameters(self, em_parameters):
        """Sets the em_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.


        :param em_parameters: The em_parameters of this RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter.  # noqa: E501
        :type: EMDefaultRequestParameters
        """

        self._em_parameters = em_parameters

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
        if issubclass(RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter, dict):
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
        if not isinstance(other, RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestParametersWrapperEMDefaultRequestParametersWhyJobParameter):
            return True

        return self.to_dict() != other.to_dict()
