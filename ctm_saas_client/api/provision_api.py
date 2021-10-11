# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.30
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ctm_saas_client.api_client import ApiClient


class ProvisionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_images(self, os, **kwargs):  # noqa: E501
        """get list of available images for the requested OS  # noqa: E501

        Get a list of the images in the system for the requested OS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_images(os, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The OS name of the requested images. (required)
        :param str version: filter according to specific version.
        :return: StringListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_images_with_http_info(os, **kwargs)  # noqa: E501
        else:
            (data) = self.get_images_with_http_info(os, **kwargs)  # noqa: E501
            return data

    def get_images_with_http_info(self, os, **kwargs):  # noqa: E501
        """get list of available images for the requested OS  # noqa: E501

        Get a list of the images in the system for the requested OS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_images_with_http_info(os, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str os: The OS name of the requested images. (required)
        :param str version: filter according to specific version.
        :return: StringListResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['os', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_images" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'os' is set
        if self.api_client.client_side_validation and ('os' not in params or
                                                       params['os'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `os` when calling `get_images`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'os' in params:
            path_params['os'] = params['os']  # noqa: E501

        query_params = []
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/provision/images/{os}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StringListResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
