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


class BuildApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def build_file(self, definitions_file, **kwargs):  # noqa: E501
        """Compile definitions file to check its validity  # noqa: E501

        Compile the provided definition file (JSON or zip) to verify it is valid for Control-M.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.build_file(definitions_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file definitions_file: A file that contains definitions to be compiled. Can be either a JSON definition file, or a zip file that contains multiple JSON definition files. (required)
        :param file deploy_descriptor_file: Deploy Descriptor JSON file.
        :return: list[DeploymentFileResults]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.build_file_with_http_info(definitions_file, **kwargs)  # noqa: E501
        else:
            (data) = self.build_file_with_http_info(definitions_file, **kwargs)  # noqa: E501
            return data

    def build_file_with_http_info(self, definitions_file, **kwargs):  # noqa: E501
        """Compile definitions file to check its validity  # noqa: E501

        Compile the provided definition file (JSON or zip) to verify it is valid for Control-M.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.build_file_with_http_info(definitions_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file definitions_file: A file that contains definitions to be compiled. Can be either a JSON definition file, or a zip file that contains multiple JSON definition files. (required)
        :param file deploy_descriptor_file: Deploy Descriptor JSON file.
        :return: list[DeploymentFileResults]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['definitions_file', 'deploy_descriptor_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method build_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'definitions_file' is set
        if self.api_client.client_side_validation and ('definitions_file' not in params or
                                                       params['definitions_file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `definitions_file` when calling `build_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'definitions_file' in params:
            local_var_files['definitionsFile'] = params['definitions_file']  # noqa: E501
        if 'deploy_descriptor_file' in params:
            local_var_files['deployDescriptorFile'] = params['deploy_descriptor_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/build', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DeploymentFileResults]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
