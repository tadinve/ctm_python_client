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


class JobStatusResult(object):
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
        "statuses": "list[JobRunStatus]",
        "start_index": "int",
        "items_per_page": "int",
        "returned": "int",
        "total": "int",
        "sort": "str",
        "next_uri": "str",
        "prev_uri": "str",
        "monitor_page_uri": "str",
    }

    attribute_map = {
        "statuses": "statuses",
        "start_index": "startIndex",
        "items_per_page": "itemsPerPage",
        "returned": "returned",
        "total": "total",
        "sort": "sort",
        "next_uri": "nextURI",
        "prev_uri": "prevURI",
        "monitor_page_uri": "monitorPageURI",
    }

    def __init__(
        self,
        statuses=None,
        start_index=None,
        items_per_page=None,
        returned=None,
        total=None,
        sort=None,
        next_uri=None,
        prev_uri=None,
        monitor_page_uri=None,
        _configuration=None,
    ):  # noqa: E501
        """JobStatusResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._statuses = None
        self._start_index = None
        self._items_per_page = None
        self._returned = None
        self._total = None
        self._sort = None
        self._next_uri = None
        self._prev_uri = None
        self._monitor_page_uri = None
        self.discriminator = None

        if statuses is not None:
            self.statuses = statuses
        if start_index is not None:
            self.start_index = start_index
        if items_per_page is not None:
            self.items_per_page = items_per_page
        if returned is not None:
            self.returned = returned
        if total is not None:
            self.total = total
        if sort is not None:
            self.sort = sort
        if next_uri is not None:
            self.next_uri = next_uri
        if prev_uri is not None:
            self.prev_uri = prev_uri
        if monitor_page_uri is not None:
            self.monitor_page_uri = monitor_page_uri

    @property
    def statuses(self):
        """Gets the statuses of this JobStatusResult.  # noqa: E501

        The list of statuses tracked by the given runId.  # noqa: E501

        :return: The statuses of this JobStatusResult.  # noqa: E501
        :rtype: list[JobRunStatus]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this JobStatusResult.

        The list of statuses tracked by the given runId.  # noqa: E501

        :param statuses: The statuses of this JobStatusResult.  # noqa: E501
        :type: list[JobRunStatus]
        """

        self._statuses = statuses

    @property
    def start_index(self):
        """Gets the start_index of this JobStatusResult.  # noqa: E501

        The index of the first item in the list.  # noqa: E501

        :return: The start_index of this JobStatusResult.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this JobStatusResult.

        The index of the first item in the list.  # noqa: E501

        :param start_index: The start_index of this JobStatusResult.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def items_per_page(self):
        """Gets the items_per_page of this JobStatusResult.  # noqa: E501

        The maximum number of items returned by each status request.  # noqa: E501

        :return: The items_per_page of this JobStatusResult.  # noqa: E501
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        """Sets the items_per_page of this JobStatusResult.

        The maximum number of items returned by each status request.  # noqa: E501

        :param items_per_page: The items_per_page of this JobStatusResult.  # noqa: E501
        :type: int
        """

        self._items_per_page = items_per_page

    @property
    def returned(self):
        """Gets the returned of this JobStatusResult.  # noqa: E501

        The number of the return items by the search.  # noqa: E501

        :return: The returned of this JobStatusResult.  # noqa: E501
        :rtype: int
        """
        return self._returned

    @returned.setter
    def returned(self, returned):
        """Sets the returned of this JobStatusResult.

        The number of the return items by the search.  # noqa: E501

        :param returned: The returned of this JobStatusResult.  # noqa: E501
        :type: int
        """

        self._returned = returned

    @property
    def total(self):
        """Gets the total of this JobStatusResult.  # noqa: E501

        The total number of items.  # noqa: E501

        :return: The total of this JobStatusResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this JobStatusResult.

        The total number of items.  # noqa: E501

        :param total: The total of this JobStatusResult.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def sort(self):
        """Gets the sort of this JobStatusResult.  # noqa: E501

        The field the list is sorted by.  # noqa: E501

        :return: The sort of this JobStatusResult.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this JobStatusResult.

        The field the list is sorted by.  # noqa: E501

        :param sort: The sort of this JobStatusResult.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def next_uri(self):
        """Gets the next_uri of this JobStatusResult.  # noqa: E501

        URI to get the next items in the list, if any.  # noqa: E501

        :return: The next_uri of this JobStatusResult.  # noqa: E501
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """Sets the next_uri of this JobStatusResult.

        URI to get the next items in the list, if any.  # noqa: E501

        :param next_uri: The next_uri of this JobStatusResult.  # noqa: E501
        :type: str
        """

        self._next_uri = next_uri

    @property
    def prev_uri(self):
        """Gets the prev_uri of this JobStatusResult.  # noqa: E501

        URI to get the previous items in the list, if any.  # noqa: E501

        :return: The prev_uri of this JobStatusResult.  # noqa: E501
        :rtype: str
        """
        return self._prev_uri

    @prev_uri.setter
    def prev_uri(self, prev_uri):
        """Sets the prev_uri of this JobStatusResult.

        URI to get the previous items in the list, if any.  # noqa: E501

        :param prev_uri: The prev_uri of this JobStatusResult.  # noqa: E501
        :type: str
        """

        self._prev_uri = prev_uri

    @property
    def monitor_page_uri(self):
        """Gets the monitor_page_uri of this JobStatusResult.  # noqa: E501

        A URI to a page displaying the workflow run live.  # noqa: E501

        :return: The monitor_page_uri of this JobStatusResult.  # noqa: E501
        :rtype: str
        """
        return self._monitor_page_uri

    @monitor_page_uri.setter
    def monitor_page_uri(self, monitor_page_uri):
        """Sets the monitor_page_uri of this JobStatusResult.

        A URI to a page displaying the workflow run live.  # noqa: E501

        :param monitor_page_uri: The monitor_page_uri of this JobStatusResult.  # noqa: E501
        :type: str
        """

        self._monitor_page_uri = monitor_page_uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(JobStatusResult, dict):
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
        if not isinstance(other, JobStatusResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobStatusResult):
            return True

        return self.to_dict() != other.to_dict()
