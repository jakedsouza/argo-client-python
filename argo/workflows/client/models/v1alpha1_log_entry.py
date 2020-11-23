# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.11.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1alpha1LogEntry(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'content': 'str',
        'pod_name': 'str'
    }

    attribute_map = {
        'content': 'content',
        'pod_name': 'podName'
    }

    def __init__(self, content=None, pod_name=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1LogEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._pod_name = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if pod_name is not None:
            self.pod_name = pod_name

    @property
    def content(self):
        """Gets the content of this V1alpha1LogEntry.  # noqa: E501


        :return: The content of this V1alpha1LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this V1alpha1LogEntry.


        :param content: The content of this V1alpha1LogEntry.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def pod_name(self):
        """Gets the pod_name of this V1alpha1LogEntry.  # noqa: E501


        :return: The pod_name of this V1alpha1LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this V1alpha1LogEntry.


        :param pod_name: The pod_name of this V1alpha1LogEntry.  # noqa: E501
        :type: str
        """

        self._pod_name = pod_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1LogEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1LogEntry):
            return True

        return self.to_dict() != other.to_dict()
