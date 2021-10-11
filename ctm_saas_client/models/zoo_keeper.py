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


class ZooKeeper(object):
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
        'zookeeper_id': 'int',
        'zookeeper_server_host': 'str',
        'zookeeper_admin_server_port': 'int',
        'zookeeper_client_port': 'int',
        'zookeeper_leader_port': 'int',
        'zookeeper_leader_election_port': 'int'
    }

    attribute_map = {
        'zookeeper_id': 'zookeeperId',
        'zookeeper_server_host': 'zookeeperServerHost',
        'zookeeper_admin_server_port': 'zookeeperAdminServerPort',
        'zookeeper_client_port': 'zookeeperClientPort',
        'zookeeper_leader_port': 'zookeeperLeaderPort',
        'zookeeper_leader_election_port': 'zookeeperLeaderElectionPort'
    }

    def __init__(self, zookeeper_id=None, zookeeper_server_host=None, zookeeper_admin_server_port=None, zookeeper_client_port=None, zookeeper_leader_port=None, zookeeper_leader_election_port=None, _configuration=None):  # noqa: E501
        """ZooKeeper - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._zookeeper_id = None
        self._zookeeper_server_host = None
        self._zookeeper_admin_server_port = None
        self._zookeeper_client_port = None
        self._zookeeper_leader_port = None
        self._zookeeper_leader_election_port = None
        self.discriminator = None

        if zookeeper_id is not None:
            self.zookeeper_id = zookeeper_id
        if zookeeper_server_host is not None:
            self.zookeeper_server_host = zookeeper_server_host
        if zookeeper_admin_server_port is not None:
            self.zookeeper_admin_server_port = zookeeper_admin_server_port
        if zookeeper_client_port is not None:
            self.zookeeper_client_port = zookeeper_client_port
        if zookeeper_leader_port is not None:
            self.zookeeper_leader_port = zookeeper_leader_port
        if zookeeper_leader_election_port is not None:
            self.zookeeper_leader_election_port = zookeeper_leader_election_port

    @property
    def zookeeper_id(self):
        """Gets the zookeeper_id of this ZooKeeper.  # noqa: E501

        zookeeper Id  # noqa: E501

        :return: The zookeeper_id of this ZooKeeper.  # noqa: E501
        :rtype: int
        """
        return self._zookeeper_id

    @zookeeper_id.setter
    def zookeeper_id(self, zookeeper_id):
        """Sets the zookeeper_id of this ZooKeeper.

        zookeeper Id  # noqa: E501

        :param zookeeper_id: The zookeeper_id of this ZooKeeper.  # noqa: E501
        :type: int
        """

        self._zookeeper_id = zookeeper_id

    @property
    def zookeeper_server_host(self):
        """Gets the zookeeper_server_host of this ZooKeeper.  # noqa: E501

        zookeeper Server Host  # noqa: E501

        :return: The zookeeper_server_host of this ZooKeeper.  # noqa: E501
        :rtype: str
        """
        return self._zookeeper_server_host

    @zookeeper_server_host.setter
    def zookeeper_server_host(self, zookeeper_server_host):
        """Sets the zookeeper_server_host of this ZooKeeper.

        zookeeper Server Host  # noqa: E501

        :param zookeeper_server_host: The zookeeper_server_host of this ZooKeeper.  # noqa: E501
        :type: str
        """

        self._zookeeper_server_host = zookeeper_server_host

    @property
    def zookeeper_admin_server_port(self):
        """Gets the zookeeper_admin_server_port of this ZooKeeper.  # noqa: E501

        zookeeper Admin Server Port  # noqa: E501

        :return: The zookeeper_admin_server_port of this ZooKeeper.  # noqa: E501
        :rtype: int
        """
        return self._zookeeper_admin_server_port

    @zookeeper_admin_server_port.setter
    def zookeeper_admin_server_port(self, zookeeper_admin_server_port):
        """Sets the zookeeper_admin_server_port of this ZooKeeper.

        zookeeper Admin Server Port  # noqa: E501

        :param zookeeper_admin_server_port: The zookeeper_admin_server_port of this ZooKeeper.  # noqa: E501
        :type: int
        """

        self._zookeeper_admin_server_port = zookeeper_admin_server_port

    @property
    def zookeeper_client_port(self):
        """Gets the zookeeper_client_port of this ZooKeeper.  # noqa: E501

        zookeeper Client Port  # noqa: E501

        :return: The zookeeper_client_port of this ZooKeeper.  # noqa: E501
        :rtype: int
        """
        return self._zookeeper_client_port

    @zookeeper_client_port.setter
    def zookeeper_client_port(self, zookeeper_client_port):
        """Sets the zookeeper_client_port of this ZooKeeper.

        zookeeper Client Port  # noqa: E501

        :param zookeeper_client_port: The zookeeper_client_port of this ZooKeeper.  # noqa: E501
        :type: int
        """

        self._zookeeper_client_port = zookeeper_client_port

    @property
    def zookeeper_leader_port(self):
        """Gets the zookeeper_leader_port of this ZooKeeper.  # noqa: E501

        zookeeper Leader Port  # noqa: E501

        :return: The zookeeper_leader_port of this ZooKeeper.  # noqa: E501
        :rtype: int
        """
        return self._zookeeper_leader_port

    @zookeeper_leader_port.setter
    def zookeeper_leader_port(self, zookeeper_leader_port):
        """Sets the zookeeper_leader_port of this ZooKeeper.

        zookeeper Leader Port  # noqa: E501

        :param zookeeper_leader_port: The zookeeper_leader_port of this ZooKeeper.  # noqa: E501
        :type: int
        """

        self._zookeeper_leader_port = zookeeper_leader_port

    @property
    def zookeeper_leader_election_port(self):
        """Gets the zookeeper_leader_election_port of this ZooKeeper.  # noqa: E501

        zookeeper Leader Election Port  # noqa: E501

        :return: The zookeeper_leader_election_port of this ZooKeeper.  # noqa: E501
        :rtype: int
        """
        return self._zookeeper_leader_election_port

    @zookeeper_leader_election_port.setter
    def zookeeper_leader_election_port(self, zookeeper_leader_election_port):
        """Sets the zookeeper_leader_election_port of this ZooKeeper.

        zookeeper Leader Election Port  # noqa: E501

        :param zookeeper_leader_election_port: The zookeeper_leader_election_port of this ZooKeeper.  # noqa: E501
        :type: int
        """

        self._zookeeper_leader_election_port = zookeeper_leader_election_port

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
        if issubclass(ZooKeeper, dict):
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
        if not isinstance(other, ZooKeeper):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZooKeeper):
            return True

        return self.to_dict() != other.to_dict()
