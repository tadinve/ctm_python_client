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

from ctm-python-client.ctm_api_client.configuration import Configuration


class UserAllowedFoldersProperties(object):
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
        'allowed_folders_names': 'list[str]',
        'as2_certificate_alias': 'str',
        'as2_id': 'str',
        'as2_public_key_certificate': 'str',
        'as2_target_folder': 'str',
        'company': 'str',
        'description': 'str',
        'email': 'str',
        'full_name': 'str',
        'hashed_password': 'str',
        'is_ldap_auth': 'int',
        'name': 'str',
        'phone_number': 'str',
        'ssh_public_key': 'str',
        'is_locked': 'bool',
        'lock_reason': 'str',
        'change_password_at_next_login': 'bool',
        'password_never_expires': 'bool',
        'last_successful_login_time': 'str'
    }

    attribute_map = {
        'allowed_folders_names': 'allowedFoldersNames',
        'as2_certificate_alias': 'as2CertificateAlias',
        'as2_id': 'as2Id',
        'as2_public_key_certificate': 'as2PublicKeyCertificate',
        'as2_target_folder': 'as2TargetFolder',
        'company': 'company',
        'description': 'description',
        'email': 'email',
        'full_name': 'fullName',
        'hashed_password': 'hashedPassword',
        'is_ldap_auth': 'isLdapAuth',
        'name': 'name',
        'phone_number': 'phoneNumber',
        'ssh_public_key': 'sshPublicKey',
        'is_locked': 'isLocked',
        'lock_reason': 'lockReason',
        'change_password_at_next_login': 'changePasswordAtNextLogin',
        'password_never_expires': 'passwordNeverExpires',
        'last_successful_login_time': 'lastSuccessfulLoginTime'
    }

    def __init__(self, allowed_folders_names=None, as2_certificate_alias=None, as2_id=None, as2_public_key_certificate=None, as2_target_folder=None, company=None, description=None, email=None, full_name=None, hashed_password=None, is_ldap_auth=None, name=None, phone_number=None, ssh_public_key=None, is_locked=None, lock_reason=None, change_password_at_next_login=None, password_never_expires=None, last_successful_login_time=None, _configuration=None):  # noqa: E501
        """UserAllowedFoldersProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allowed_folders_names = None
        self._as2_certificate_alias = None
        self._as2_id = None
        self._as2_public_key_certificate = None
        self._as2_target_folder = None
        self._company = None
        self._description = None
        self._email = None
        self._full_name = None
        self._hashed_password = None
        self._is_ldap_auth = None
        self._name = None
        self._phone_number = None
        self._ssh_public_key = None
        self._is_locked = None
        self._lock_reason = None
        self._change_password_at_next_login = None
        self._password_never_expires = None
        self._last_successful_login_time = None
        self.discriminator = None

        if allowed_folders_names is not None:
            self.allowed_folders_names = allowed_folders_names
        if as2_certificate_alias is not None:
            self.as2_certificate_alias = as2_certificate_alias
        if as2_id is not None:
            self.as2_id = as2_id
        if as2_public_key_certificate is not None:
            self.as2_public_key_certificate = as2_public_key_certificate
        if as2_target_folder is not None:
            self.as2_target_folder = as2_target_folder
        if company is not None:
            self.company = company
        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if hashed_password is not None:
            self.hashed_password = hashed_password
        if is_ldap_auth is not None:
            self.is_ldap_auth = is_ldap_auth
        if name is not None:
            self.name = name
        if phone_number is not None:
            self.phone_number = phone_number
        if ssh_public_key is not None:
            self.ssh_public_key = ssh_public_key
        if is_locked is not None:
            self.is_locked = is_locked
        if lock_reason is not None:
            self.lock_reason = lock_reason
        if change_password_at_next_login is not None:
            self.change_password_at_next_login = change_password_at_next_login
        if password_never_expires is not None:
            self.password_never_expires = password_never_expires
        if last_successful_login_time is not None:
            self.last_successful_login_time = last_successful_login_time

    @property
    def allowed_folders_names(self):
        """Gets the allowed_folders_names of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The allowed_folders_names of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_folders_names

    @allowed_folders_names.setter
    def allowed_folders_names(self, allowed_folders_names):
        """Sets the allowed_folders_names of this UserAllowedFoldersProperties.


        :param allowed_folders_names: The allowed_folders_names of this UserAllowedFoldersProperties.  # noqa: E501
        :type: list[str]
        """

        self._allowed_folders_names = allowed_folders_names

    @property
    def as2_certificate_alias(self):
        """Gets the as2_certificate_alias of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The as2_certificate_alias of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._as2_certificate_alias

    @as2_certificate_alias.setter
    def as2_certificate_alias(self, as2_certificate_alias):
        """Sets the as2_certificate_alias of this UserAllowedFoldersProperties.


        :param as2_certificate_alias: The as2_certificate_alias of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._as2_certificate_alias = as2_certificate_alias

    @property
    def as2_id(self):
        """Gets the as2_id of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The as2_id of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._as2_id

    @as2_id.setter
    def as2_id(self, as2_id):
        """Sets the as2_id of this UserAllowedFoldersProperties.


        :param as2_id: The as2_id of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._as2_id = as2_id

    @property
    def as2_public_key_certificate(self):
        """Gets the as2_public_key_certificate of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The as2_public_key_certificate of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._as2_public_key_certificate

    @as2_public_key_certificate.setter
    def as2_public_key_certificate(self, as2_public_key_certificate):
        """Sets the as2_public_key_certificate of this UserAllowedFoldersProperties.


        :param as2_public_key_certificate: The as2_public_key_certificate of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._as2_public_key_certificate = as2_public_key_certificate

    @property
    def as2_target_folder(self):
        """Gets the as2_target_folder of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The as2_target_folder of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._as2_target_folder

    @as2_target_folder.setter
    def as2_target_folder(self, as2_target_folder):
        """Sets the as2_target_folder of this UserAllowedFoldersProperties.


        :param as2_target_folder: The as2_target_folder of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._as2_target_folder = as2_target_folder

    @property
    def company(self):
        """Gets the company of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The company of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UserAllowedFoldersProperties.


        :param company: The company of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def description(self):
        """Gets the description of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The description of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserAllowedFoldersProperties.


        :param description: The description of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email(self):
        """Gets the email of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The email of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserAllowedFoldersProperties.


        :param email: The email of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The full_name of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserAllowedFoldersProperties.


        :param full_name: The full_name of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def hashed_password(self):
        """Gets the hashed_password of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The hashed_password of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, hashed_password):
        """Sets the hashed_password of this UserAllowedFoldersProperties.


        :param hashed_password: The hashed_password of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._hashed_password = hashed_password

    @property
    def is_ldap_auth(self):
        """Gets the is_ldap_auth of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The is_ldap_auth of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: int
        """
        return self._is_ldap_auth

    @is_ldap_auth.setter
    def is_ldap_auth(self, is_ldap_auth):
        """Sets the is_ldap_auth of this UserAllowedFoldersProperties.


        :param is_ldap_auth: The is_ldap_auth of this UserAllowedFoldersProperties.  # noqa: E501
        :type: int
        """

        self._is_ldap_auth = is_ldap_auth

    @property
    def name(self):
        """Gets the name of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The name of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserAllowedFoldersProperties.


        :param name: The name of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_number(self):
        """Gets the phone_number of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The phone_number of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this UserAllowedFoldersProperties.


        :param phone_number: The phone_number of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def ssh_public_key(self):
        """Gets the ssh_public_key of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The ssh_public_key of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """Sets the ssh_public_key of this UserAllowedFoldersProperties.


        :param ssh_public_key: The ssh_public_key of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._ssh_public_key = ssh_public_key

    @property
    def is_locked(self):
        """Gets the is_locked of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The is_locked of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this UserAllowedFoldersProperties.


        :param is_locked: The is_locked of this UserAllowedFoldersProperties.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def lock_reason(self):
        """Gets the lock_reason of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The lock_reason of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this UserAllowedFoldersProperties.


        :param lock_reason: The lock_reason of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._lock_reason = lock_reason

    @property
    def change_password_at_next_login(self):
        """Gets the change_password_at_next_login of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The change_password_at_next_login of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: bool
        """
        return self._change_password_at_next_login

    @change_password_at_next_login.setter
    def change_password_at_next_login(self, change_password_at_next_login):
        """Sets the change_password_at_next_login of this UserAllowedFoldersProperties.


        :param change_password_at_next_login: The change_password_at_next_login of this UserAllowedFoldersProperties.  # noqa: E501
        :type: bool
        """

        self._change_password_at_next_login = change_password_at_next_login

    @property
    def password_never_expires(self):
        """Gets the password_never_expires of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The password_never_expires of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: bool
        """
        return self._password_never_expires

    @password_never_expires.setter
    def password_never_expires(self, password_never_expires):
        """Sets the password_never_expires of this UserAllowedFoldersProperties.


        :param password_never_expires: The password_never_expires of this UserAllowedFoldersProperties.  # noqa: E501
        :type: bool
        """

        self._password_never_expires = password_never_expires

    @property
    def last_successful_login_time(self):
        """Gets the last_successful_login_time of this UserAllowedFoldersProperties.  # noqa: E501


        :return: The last_successful_login_time of this UserAllowedFoldersProperties.  # noqa: E501
        :rtype: str
        """
        return self._last_successful_login_time

    @last_successful_login_time.setter
    def last_successful_login_time(self, last_successful_login_time):
        """Sets the last_successful_login_time of this UserAllowedFoldersProperties.


        :param last_successful_login_time: The last_successful_login_time of this UserAllowedFoldersProperties.  # noqa: E501
        :type: str
        """

        self._last_successful_login_time = last_successful_login_time

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
        if issubclass(UserAllowedFoldersProperties, dict):
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
        if not isinstance(other, UserAllowedFoldersProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAllowedFoldersProperties):
            return True

        return self.to_dict() != other.to_dict()
