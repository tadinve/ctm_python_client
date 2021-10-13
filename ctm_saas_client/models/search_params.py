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


class SearchParams(object):
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
        'ctm': 'str',
        'job_name': 'str',
        'app': 'str',
        'sub_app': 'str',
        'folder': 'str',
        'status': 'str',
        'lib': 'str',
        'limit': 'int',
        'log_contains': 'str',
        'output_contains': 'str',
        'mem_lib': 'str',
        'mem_name': 'str',
        'node_group': 'str',
        'node_id': 'str',
        'from_order_date': 'str',
        'to_order_date': 'str',
        'order_id': 'str',
        'run_as': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'ctm': 'ctm',
        'job_name': 'jobName',
        'app': 'app',
        'sub_app': 'subApp',
        'folder': 'folder',
        'status': 'status',
        'lib': 'lib',
        'limit': 'limit',
        'log_contains': 'logContains',
        'output_contains': 'outputContains',
        'mem_lib': 'memLib',
        'mem_name': 'memName',
        'node_group': 'nodeGroup',
        'node_id': 'nodeId',
        'from_order_date': 'fromOrderDate',
        'to_order_date': 'toOrderDate',
        'order_id': 'orderId',
        'run_as': 'runAs',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, ctm=None, job_name=None, app=None, sub_app=None, folder=None, status=None, lib=None, limit=None, log_contains=None, output_contains=None, mem_lib=None, mem_name=None, node_group=None, node_id=None, from_order_date=None, to_order_date=None, order_id=None, run_as=None, start_date=None, end_date=None, _configuration=None):  # noqa: E501
        """SearchParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ctm = None
        self._job_name = None
        self._app = None
        self._sub_app = None
        self._folder = None
        self._status = None
        self._lib = None
        self._limit = None
        self._log_contains = None
        self._output_contains = None
        self._mem_lib = None
        self._mem_name = None
        self._node_group = None
        self._node_id = None
        self._from_order_date = None
        self._to_order_date = None
        self._order_id = None
        self._run_as = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if ctm is not None:
            self.ctm = ctm
        if job_name is not None:
            self.job_name = job_name
        if app is not None:
            self.app = app
        if sub_app is not None:
            self.sub_app = sub_app
        if folder is not None:
            self.folder = folder
        if status is not None:
            self.status = status
        if lib is not None:
            self.lib = lib
        if limit is not None:
            self.limit = limit
        if log_contains is not None:
            self.log_contains = log_contains
        if output_contains is not None:
            self.output_contains = output_contains
        if mem_lib is not None:
            self.mem_lib = mem_lib
        if mem_name is not None:
            self.mem_name = mem_name
        if node_group is not None:
            self.node_group = node_group
        if node_id is not None:
            self.node_id = node_id
        if from_order_date is not None:
            self.from_order_date = from_order_date
        if to_order_date is not None:
            self.to_order_date = to_order_date
        if order_id is not None:
            self.order_id = order_id
        if run_as is not None:
            self.run_as = run_as
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def ctm(self):
        """Gets the ctm of this SearchParams.  # noqa: E501

        The name of sthe Control-M server in which the job was ordered from. HIDDEN.  # noqa: E501

        :return: The ctm of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this SearchParams.

        The name of sthe Control-M server in which the job was ordered from. HIDDEN.  # noqa: E501

        :param ctm: The ctm of this SearchParams.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def job_name(self):
        """Gets the job_name of this SearchParams.  # noqa: E501

        The name of the job. HIDDEN.  # noqa: E501

        :return: The job_name of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this SearchParams.

        The name of the job. HIDDEN.  # noqa: E501

        :param job_name: The job_name of this SearchParams.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def app(self):
        """Gets the app of this SearchParams.  # noqa: E501

        The name of the application the jobs belong to. HIDDEN.  # noqa: E501

        :return: The app of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this SearchParams.

        The name of the application the jobs belong to. HIDDEN.  # noqa: E501

        :param app: The app of this SearchParams.  # noqa: E501
        :type: str
        """

        self._app = app

    @property
    def sub_app(self):
        """Gets the sub_app of this SearchParams.  # noqa: E501

        The name of the sub-application the jobs belong to. HIDDEN.  # noqa: E501

        :return: The sub_app of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._sub_app

    @sub_app.setter
    def sub_app(self, sub_app):
        """Sets the sub_app of this SearchParams.

        The name of the sub-application the jobs belong to. HIDDEN.  # noqa: E501

        :param sub_app: The sub_app of this SearchParams.  # noqa: E501
        :type: str
        """

        self._sub_app = sub_app

    @property
    def folder(self):
        """Gets the folder of this SearchParams.  # noqa: E501

        The name of the parent folder. HIDDEN.  # noqa: E501

        :return: The folder of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this SearchParams.

        The name of the parent folder. HIDDEN.  # noqa: E501

        :param folder: The folder of this SearchParams.  # noqa: E501
        :type: str
        """

        self._folder = folder

    @property
    def status(self):
        """Gets the status of this SearchParams.  # noqa: E501

        The job's end status. HIDDEN.  # noqa: E501

        :return: The status of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchParams.

        The job's end status. HIDDEN.  # noqa: E501

        :param status: The status of this SearchParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "NOTOK", "ALL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def lib(self):
        """Gets the lib of this SearchParams.  # noqa: E501

        The job's library name. HIDDEN.  # noqa: E501

        :return: The lib of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._lib

    @lib.setter
    def lib(self, lib):
        """Sets the lib of this SearchParams.

        The job's library name. HIDDEN.  # noqa: E501

        :param lib: The lib of this SearchParams.  # noqa: E501
        :type: str
        """

        self._lib = lib

    @property
    def limit(self):
        """Gets the limit of this SearchParams.  # noqa: E501

        Maximum archived Jobs to display. HIDDEN.  # noqa: E501

        :return: The limit of this SearchParams.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchParams.

        Maximum archived Jobs to display. HIDDEN.  # noqa: E501

        :param limit: The limit of this SearchParams.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def log_contains(self):
        """Gets the log_contains of this SearchParams.  # noqa: E501

        Job log must contain the given phrase. HIDDEN.  # noqa: E501

        :return: The log_contains of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._log_contains

    @log_contains.setter
    def log_contains(self, log_contains):
        """Sets the log_contains of this SearchParams.

        Job log must contain the given phrase. HIDDEN.  # noqa: E501

        :param log_contains: The log_contains of this SearchParams.  # noqa: E501
        :type: str
        """

        self._log_contains = log_contains

    @property
    def output_contains(self):
        """Gets the output_contains of this SearchParams.  # noqa: E501

        Job output must contain the given phrase. HIDDEN.  # noqa: E501

        :return: The output_contains of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._output_contains

    @output_contains.setter
    def output_contains(self, output_contains):
        """Sets the output_contains of this SearchParams.

        Job output must contain the given phrase. HIDDEN.  # noqa: E501

        :param output_contains: The output_contains of this SearchParams.  # noqa: E501
        :type: str
        """

        self._output_contains = output_contains

    @property
    def mem_lib(self):
        """Gets the mem_lib of this SearchParams.  # noqa: E501

        Member's library. HIDDEN.  # noqa: E501

        :return: The mem_lib of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._mem_lib

    @mem_lib.setter
    def mem_lib(self, mem_lib):
        """Sets the mem_lib of this SearchParams.

        Member's library. HIDDEN.  # noqa: E501

        :param mem_lib: The mem_lib of this SearchParams.  # noqa: E501
        :type: str
        """

        self._mem_lib = mem_lib

    @property
    def mem_name(self):
        """Gets the mem_name of this SearchParams.  # noqa: E501

        Member name. HIDDEN.  # noqa: E501

        :return: The mem_name of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._mem_name

    @mem_name.setter
    def mem_name(self, mem_name):
        """Sets the mem_name of this SearchParams.

        Member name. HIDDEN.  # noqa: E501

        :param mem_name: The mem_name of this SearchParams.  # noqa: E501
        :type: str
        """

        self._mem_name = mem_name

    @property
    def node_group(self):
        """Gets the node_group of this SearchParams.  # noqa: E501

        Job's node group. HIDDEN.  # noqa: E501

        :return: The node_group of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._node_group

    @node_group.setter
    def node_group(self, node_group):
        """Sets the node_group of this SearchParams.

        Job's node group. HIDDEN.  # noqa: E501

        :param node_group: The node_group of this SearchParams.  # noqa: E501
        :type: str
        """

        self._node_group = node_group

    @property
    def node_id(self):
        """Gets the node_id of this SearchParams.  # noqa: E501

        Job's node id (agent). HIDDEN.  # noqa: E501

        :return: The node_id of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this SearchParams.

        Job's node id (agent). HIDDEN.  # noqa: E501

        :param node_id: The node_id of this SearchParams.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def from_order_date(self):
        """Gets the from_order_date of this SearchParams.  # noqa: E501

        Indicating a date by which will look for jobs that their order date started afterwards. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :return: The from_order_date of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._from_order_date

    @from_order_date.setter
    def from_order_date(self, from_order_date):
        """Sets the from_order_date of this SearchParams.

        Indicating a date by which will look for jobs that their order date started afterwards. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :param from_order_date: The from_order_date of this SearchParams.  # noqa: E501
        :type: str
        """

        self._from_order_date = from_order_date

    @property
    def to_order_date(self):
        """Gets the to_order_date of this SearchParams.  # noqa: E501

        Indicating a date by which will look for jobs that their order date ended before. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :return: The to_order_date of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._to_order_date

    @to_order_date.setter
    def to_order_date(self, to_order_date):
        """Sets the to_order_date of this SearchParams.

        Indicating a date by which will look for jobs that their order date ended before. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :param to_order_date: The to_order_date of this SearchParams.  # noqa: E501
        :type: str
        """

        self._to_order_date = to_order_date

    @property
    def order_id(self):
        """Gets the order_id of this SearchParams.  # noqa: E501

        Job's order id. HIDDEN.  # noqa: E501

        :return: The order_id of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this SearchParams.

        Job's order id. HIDDEN.  # noqa: E501

        :param order_id: The order_id of this SearchParams.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def run_as(self):
        """Gets the run_as of this SearchParams.  # noqa: E501

        Runs as (username on agent machine). HIDDEN.  # noqa: E501

        :return: The run_as of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._run_as

    @run_as.setter
    def run_as(self, run_as):
        """Sets the run_as of this SearchParams.

        Runs as (username on agent machine). HIDDEN.  # noqa: E501

        :param run_as: The run_as of this SearchParams.  # noqa: E501
        :type: str
        """

        self._run_as = run_as

    @property
    def start_date(self):
        """Gets the start_date of this SearchParams.  # noqa: E501

        Job execution start date. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :return: The start_date of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SearchParams.

        Job execution start date. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :param start_date: The start_date of this SearchParams.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SearchParams.  # noqa: E501

        Job execution end date. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :return: The end_date of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SearchParams.

        Job execution end date. Date format - YYYY-MM-DD. HIDDEN.  # noqa: E501

        :param end_date: The end_date of this SearchParams.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

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
        if issubclass(SearchParams, dict):
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
        if not isinstance(other, SearchParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchParams):
            return True

        return self.to_dict() != other.to_dict()
