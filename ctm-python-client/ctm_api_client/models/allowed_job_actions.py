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


class AllowedJobActions(object):
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
        'view_properties': 'bool',
        'documentation': 'bool',
        'log': 'bool',
        'statistics': 'bool',
        'view_output_list': 'bool',
        'view_jcl': 'bool',
        'why': 'bool',
        'hold': 'bool',
        'free': 'bool',
        'confirm': 'bool',
        'rerun': 'bool',
        'react': 'bool',
        'restart': 'bool',
        'kill': 'bool',
        'bypass': 'bool',
        'delete': 'bool',
        'undelete': 'bool',
        'set_to_ok': 'bool',
        'edit_properties': 'bool',
        'edit_jcl': 'bool'
    }

    attribute_map = {
        'view_properties': 'ViewProperties',
        'documentation': 'Documentation',
        'log': 'Log',
        'statistics': 'Statistics',
        'view_output_list': 'ViewOutputList',
        'view_jcl': 'ViewJcl',
        'why': 'Why',
        'hold': 'Hold',
        'free': 'Free',
        'confirm': 'Confirm',
        'rerun': 'Rerun',
        'react': 'React',
        'restart': 'Restart',
        'kill': 'Kill',
        'bypass': 'Bypass',
        'delete': 'Delete',
        'undelete': 'Undelete',
        'set_to_ok': 'SetToOk',
        'edit_properties': 'EditProperties',
        'edit_jcl': 'EditJcl'
    }

    def __init__(self, view_properties=None, documentation=None, log=None, statistics=None, view_output_list=None, view_jcl=None, why=None, hold=None, free=None, confirm=None, rerun=None, react=None, restart=None, kill=None, bypass=None, delete=None, undelete=None, set_to_ok=None, edit_properties=None, edit_jcl=None, _configuration=None):  # noqa: E501
        """AllowedJobActions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._view_properties = None
        self._documentation = None
        self._log = None
        self._statistics = None
        self._view_output_list = None
        self._view_jcl = None
        self._why = None
        self._hold = None
        self._free = None
        self._confirm = None
        self._rerun = None
        self._react = None
        self._restart = None
        self._kill = None
        self._bypass = None
        self._delete = None
        self._undelete = None
        self._set_to_ok = None
        self._edit_properties = None
        self._edit_jcl = None
        self.discriminator = None

        if view_properties is not None:
            self.view_properties = view_properties
        if documentation is not None:
            self.documentation = documentation
        if log is not None:
            self.log = log
        if statistics is not None:
            self.statistics = statistics
        if view_output_list is not None:
            self.view_output_list = view_output_list
        if view_jcl is not None:
            self.view_jcl = view_jcl
        if why is not None:
            self.why = why
        if hold is not None:
            self.hold = hold
        if free is not None:
            self.free = free
        if confirm is not None:
            self.confirm = confirm
        if rerun is not None:
            self.rerun = rerun
        if react is not None:
            self.react = react
        if restart is not None:
            self.restart = restart
        if kill is not None:
            self.kill = kill
        if bypass is not None:
            self.bypass = bypass
        if delete is not None:
            self.delete = delete
        if undelete is not None:
            self.undelete = undelete
        if set_to_ok is not None:
            self.set_to_ok = set_to_ok
        if edit_properties is not None:
            self.edit_properties = edit_properties
        if edit_jcl is not None:
            self.edit_jcl = edit_jcl

    @property
    def view_properties(self):
        """Gets the view_properties of this AllowedJobActions.  # noqa: E501

        True if Properties action is allowed  # noqa: E501

        :return: The view_properties of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._view_properties

    @view_properties.setter
    def view_properties(self, view_properties):
        """Sets the view_properties of this AllowedJobActions.

        True if Properties action is allowed  # noqa: E501

        :param view_properties: The view_properties of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._view_properties = view_properties

    @property
    def documentation(self):
        """Gets the documentation of this AllowedJobActions.  # noqa: E501

        True if Documentation action is allowed  # noqa: E501

        :return: The documentation of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation):
        """Sets the documentation of this AllowedJobActions.

        True if Documentation action is allowed  # noqa: E501

        :param documentation: The documentation of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._documentation = documentation

    @property
    def log(self):
        """Gets the log of this AllowedJobActions.  # noqa: E501

        True if Log action is allowed  # noqa: E501

        :return: The log of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this AllowedJobActions.

        True if Log action is allowed  # noqa: E501

        :param log: The log of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._log = log

    @property
    def statistics(self):
        """Gets the statistics of this AllowedJobActions.  # noqa: E501

        True if Statistics action is allowed  # noqa: E501

        :return: The statistics of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this AllowedJobActions.

        True if Statistics action is allowed  # noqa: E501

        :param statistics: The statistics of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._statistics = statistics

    @property
    def view_output_list(self):
        """Gets the view_output_list of this AllowedJobActions.  # noqa: E501

        True if ViewOutputList action is allowed  # noqa: E501

        :return: The view_output_list of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._view_output_list

    @view_output_list.setter
    def view_output_list(self, view_output_list):
        """Sets the view_output_list of this AllowedJobActions.

        True if ViewOutputList action is allowed  # noqa: E501

        :param view_output_list: The view_output_list of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._view_output_list = view_output_list

    @property
    def view_jcl(self):
        """Gets the view_jcl of this AllowedJobActions.  # noqa: E501

        True if ViewJcl action is allowed  # noqa: E501

        :return: The view_jcl of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._view_jcl

    @view_jcl.setter
    def view_jcl(self, view_jcl):
        """Sets the view_jcl of this AllowedJobActions.

        True if ViewJcl action is allowed  # noqa: E501

        :param view_jcl: The view_jcl of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._view_jcl = view_jcl

    @property
    def why(self):
        """Gets the why of this AllowedJobActions.  # noqa: E501

        True if Why action is allowed  # noqa: E501

        :return: The why of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._why

    @why.setter
    def why(self, why):
        """Sets the why of this AllowedJobActions.

        True if Why action is allowed  # noqa: E501

        :param why: The why of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._why = why

    @property
    def hold(self):
        """Gets the hold of this AllowedJobActions.  # noqa: E501

        True if Hold action is allowed  # noqa: E501

        :return: The hold of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._hold

    @hold.setter
    def hold(self, hold):
        """Sets the hold of this AllowedJobActions.

        True if Hold action is allowed  # noqa: E501

        :param hold: The hold of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._hold = hold

    @property
    def free(self):
        """Gets the free of this AllowedJobActions.  # noqa: E501

        True if Free action is allowed  # noqa: E501

        :return: The free of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this AllowedJobActions.

        True if Free action is allowed  # noqa: E501

        :param free: The free of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._free = free

    @property
    def confirm(self):
        """Gets the confirm of this AllowedJobActions.  # noqa: E501

        True if Confirm action is allowed  # noqa: E501

        :return: The confirm of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._confirm

    @confirm.setter
    def confirm(self, confirm):
        """Sets the confirm of this AllowedJobActions.

        True if Confirm action is allowed  # noqa: E501

        :param confirm: The confirm of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._confirm = confirm

    @property
    def rerun(self):
        """Gets the rerun of this AllowedJobActions.  # noqa: E501

        True if Rerun action is allowed  # noqa: E501

        :return: The rerun of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._rerun

    @rerun.setter
    def rerun(self, rerun):
        """Sets the rerun of this AllowedJobActions.

        True if Rerun action is allowed  # noqa: E501

        :param rerun: The rerun of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._rerun = rerun

    @property
    def react(self):
        """Gets the react of this AllowedJobActions.  # noqa: E501

        True if React action is allowed  # noqa: E501

        :return: The react of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._react

    @react.setter
    def react(self, react):
        """Sets the react of this AllowedJobActions.

        True if React action is allowed  # noqa: E501

        :param react: The react of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._react = react

    @property
    def restart(self):
        """Gets the restart of this AllowedJobActions.  # noqa: E501

        True if Restart action is allowed  # noqa: E501

        :return: The restart of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._restart

    @restart.setter
    def restart(self, restart):
        """Sets the restart of this AllowedJobActions.

        True if Restart action is allowed  # noqa: E501

        :param restart: The restart of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._restart = restart

    @property
    def kill(self):
        """Gets the kill of this AllowedJobActions.  # noqa: E501

        True if Kill action is allowed  # noqa: E501

        :return: The kill of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._kill

    @kill.setter
    def kill(self, kill):
        """Sets the kill of this AllowedJobActions.

        True if Kill action is allowed  # noqa: E501

        :param kill: The kill of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._kill = kill

    @property
    def bypass(self):
        """Gets the bypass of this AllowedJobActions.  # noqa: E501

        True if Bypass action is allowed  # noqa: E501

        :return: The bypass of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._bypass

    @bypass.setter
    def bypass(self, bypass):
        """Sets the bypass of this AllowedJobActions.

        True if Bypass action is allowed  # noqa: E501

        :param bypass: The bypass of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._bypass = bypass

    @property
    def delete(self):
        """Gets the delete of this AllowedJobActions.  # noqa: E501

        True if Delete action is allowed  # noqa: E501

        :return: The delete of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this AllowedJobActions.

        True if Delete action is allowed  # noqa: E501

        :param delete: The delete of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._delete = delete

    @property
    def undelete(self):
        """Gets the undelete of this AllowedJobActions.  # noqa: E501

        True if Undelete action is allowed  # noqa: E501

        :return: The undelete of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._undelete

    @undelete.setter
    def undelete(self, undelete):
        """Sets the undelete of this AllowedJobActions.

        True if Undelete action is allowed  # noqa: E501

        :param undelete: The undelete of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._undelete = undelete

    @property
    def set_to_ok(self):
        """Gets the set_to_ok of this AllowedJobActions.  # noqa: E501

        True if SetToOk action is allowed  # noqa: E501

        :return: The set_to_ok of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._set_to_ok

    @set_to_ok.setter
    def set_to_ok(self, set_to_ok):
        """Sets the set_to_ok of this AllowedJobActions.

        True if SetToOk action is allowed  # noqa: E501

        :param set_to_ok: The set_to_ok of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._set_to_ok = set_to_ok

    @property
    def edit_properties(self):
        """Gets the edit_properties of this AllowedJobActions.  # noqa: E501

        True if EditProperties action is allowed  # noqa: E501

        :return: The edit_properties of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._edit_properties

    @edit_properties.setter
    def edit_properties(self, edit_properties):
        """Sets the edit_properties of this AllowedJobActions.

        True if EditProperties action is allowed  # noqa: E501

        :param edit_properties: The edit_properties of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._edit_properties = edit_properties

    @property
    def edit_jcl(self):
        """Gets the edit_jcl of this AllowedJobActions.  # noqa: E501

        True if EditJcl action is allowed  # noqa: E501

        :return: The edit_jcl of this AllowedJobActions.  # noqa: E501
        :rtype: bool
        """
        return self._edit_jcl

    @edit_jcl.setter
    def edit_jcl(self, edit_jcl):
        """Sets the edit_jcl of this AllowedJobActions.

        True if EditJcl action is allowed  # noqa: E501

        :param edit_jcl: The edit_jcl of this AllowedJobActions.  # noqa: E501
        :type: bool
        """

        self._edit_jcl = edit_jcl

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
        if issubclass(AllowedJobActions, dict):
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
        if not isinstance(other, AllowedJobActions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllowedJobActions):
            return True

        return self.to_dict() != other.to_dict()
