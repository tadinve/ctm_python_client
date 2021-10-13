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


class ExternalUserData(object):
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
        'email': 'str',
        'company': 'str',
        'password': 'str',
        'description': 'str',
        'phone_number': 'str',
        'ssh_key': 'str',
        'as2_key': 'As2KeyData',
        'is_locked': 'bool',
        'lock_reason': 'str',
        'change_password_at_next_login': 'bool',
        'password_never_expires': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'company': 'company',
        'password': 'password',
        'description': 'description',
        'phone_number': 'phoneNumber',
        'ssh_key': 'sshKey',
        'as2_key': 'as2Key',
        'is_locked': 'isLocked',
        'lock_reason': 'lockReason',
        'change_password_at_next_login': 'changePasswordAtNextLogin',
        'password_never_expires': 'passwordNeverExpires'
    }

    def __init__(self, name=None, email=None, company=None, password=None, description=None, phone_number=None, ssh_key=None, as2_key=None, is_locked=None, lock_reason=None, change_password_at_next_login=None, password_never_expires=None, _configuration=None):  # noqa: E501
        """ExternalUserData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._email = None
        self._company = None
        self._password = None
        self._description = None
        self._phone_number = None
        self._ssh_key = None
        self._as2_key = None
        self._is_locked = None
        self._lock_reason = None
        self._change_password_at_next_login = None
        self._password_never_expires = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if company is not None:
            self.company = company
        if password is not None:
            self.password = password
        if description is not None:
            self.description = description
        if phone_number is not None:
            self.phone_number = phone_number
        if ssh_key is not None:
            self.ssh_key = ssh_key
        if as2_key is not None:
            self.as2_key = as2_key
        if is_locked is not None:
            self.is_locked = is_locked
        if lock_reason is not None:
            self.lock_reason = lock_reason
        if change_password_at_next_login is not None:
            self.change_password_at_next_login = change_password_at_next_login
        if password_never_expires is not None:
            self.password_never_expires = password_never_expires

    @property
    def name(self):
        """Gets the name of this ExternalUserData.  # noqa: E501

        external user name REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN  # noqa: E501

        :return: The name of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalUserData.

        external user name REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN  # noqa: E501

        :param name: The name of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this ExternalUserData.  # noqa: E501

        user email REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN  # noqa: E501

        :return: The email of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ExternalUserData.

        user email REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN  # noqa: E501

        :param email: The email of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def company(self):
        """Gets the company of this ExternalUserData.  # noqa: E501

        user's company REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN  # noqa: E501

        :return: The company of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ExternalUserData.

        user's company REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN  # noqa: E501

        :param company: The company of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def password(self):
        """Gets the password of this ExternalUserData.  # noqa: E501

        user password HIDDEN:updateExternalUser,updateExternalUserForSite  # noqa: E501

        :return: The password of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ExternalUserData.

        user password HIDDEN:updateExternalUser,updateExternalUserForSite  # noqa: E501

        :param password: The password of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def description(self):
        """Gets the description of this ExternalUserData.  # noqa: E501

        user description HIDDEN  # noqa: E501

        :return: The description of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalUserData.

        user description HIDDEN  # noqa: E501

        :param description: The description of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def phone_number(self):
        """Gets the phone_number of this ExternalUserData.  # noqa: E501

        external user phone number HIDDEN  # noqa: E501

        :return: The phone_number of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ExternalUserData.

        external user phone number HIDDEN  # noqa: E501

        :param phone_number: The phone_number of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def ssh_key(self):
        """Gets the ssh_key of this ExternalUserData.  # noqa: E501

        SSH key string HIDDEN  # noqa: E501

        :return: The ssh_key of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._ssh_key

    @ssh_key.setter
    def ssh_key(self, ssh_key):
        """Sets the ssh_key of this ExternalUserData.

        SSH key string HIDDEN  # noqa: E501

        :param ssh_key: The ssh_key of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._ssh_key = ssh_key

    @property
    def as2_key(self):
        """Gets the as2_key of this ExternalUserData.  # noqa: E501

        AS2 key string HIDDEN  # noqa: E501

        :return: The as2_key of this ExternalUserData.  # noqa: E501
        :rtype: As2KeyData
        """
        return self._as2_key

    @as2_key.setter
    def as2_key(self, as2_key):
        """Sets the as2_key of this ExternalUserData.

        AS2 key string HIDDEN  # noqa: E501

        :param as2_key: The as2_key of this ExternalUserData.  # noqa: E501
        :type: As2KeyData
        """

        self._as2_key = as2_key

    @property
    def is_locked(self):
        """Gets the is_locked of this ExternalUserData.  # noqa: E501

        indicates whether the user account is locked HIDDEN  # noqa: E501

        :return: The is_locked of this ExternalUserData.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this ExternalUserData.

        indicates whether the user account is locked HIDDEN  # noqa: E501

        :param is_locked: The is_locked of this ExternalUserData.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def lock_reason(self):
        """Gets the lock_reason of this ExternalUserData.  # noqa: E501

        provides the reason for locking the user account HIDDEN  # noqa: E501

        :return: The lock_reason of this ExternalUserData.  # noqa: E501
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this ExternalUserData.

        provides the reason for locking the user account HIDDEN  # noqa: E501

        :param lock_reason: The lock_reason of this ExternalUserData.  # noqa: E501
        :type: str
        """

        self._lock_reason = lock_reason

    @property
    def change_password_at_next_login(self):
        """Gets the change_password_at_next_login of this ExternalUserData.  # noqa: E501

        indicates whether a password change is required at next login HIDDEN  # noqa: E501

        :return: The change_password_at_next_login of this ExternalUserData.  # noqa: E501
        :rtype: bool
        """
        return self._change_password_at_next_login

    @change_password_at_next_login.setter
    def change_password_at_next_login(self, change_password_at_next_login):
        """Sets the change_password_at_next_login of this ExternalUserData.

        indicates whether a password change is required at next login HIDDEN  # noqa: E501

        :param change_password_at_next_login: The change_password_at_next_login of this ExternalUserData.  # noqa: E501
        :type: bool
        """

        self._change_password_at_next_login = change_password_at_next_login

    @property
    def password_never_expires(self):
        """Gets the password_never_expires of this ExternalUserData.  # noqa: E501

        indicates whether the user's password is set to never expire HIDDEN  # noqa: E501

        :return: The password_never_expires of this ExternalUserData.  # noqa: E501
        :rtype: bool
        """
        return self._password_never_expires

    @password_never_expires.setter
    def password_never_expires(self, password_never_expires):
        """Sets the password_never_expires of this ExternalUserData.

        indicates whether the user's password is set to never expire HIDDEN  # noqa: E501

        :param password_never_expires: The password_never_expires of this ExternalUserData.  # noqa: E501
        :type: bool
        """

        self._password_never_expires = password_never_expires

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
        if issubclass(ExternalUserData, dict):
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
        if not isinstance(other, ExternalUserData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalUserData):
            return True

        return self.to_dict() != other.to_dict()
