# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ActionIn(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ActionIn - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'ActionDetailsArray',
            'cid': 'str',
            'ddid': 'str',
            'sdid': 'str',
            'ts': 'int',
            'type': 'str'
        }

        self.attribute_map = {
            'data': 'data',
            'cid': 'cid',
            'ddid': 'ddid',
            'sdid': 'sdid',
            'ts': 'ts',
            'type': 'type'
        }

        self._data = None
        self._cid = None
        self._ddid = None
        self._sdid = None
        self._ts = None
        self._type = 'action'

    @property
    def data(self):
        """
        Gets the data of this ActionIn.


        :return: The data of this ActionIn.
        :rtype: ActionDetailsArray
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this ActionIn.


        :param data: The data of this ActionIn.
        :type: ActionDetailsArray
        """
        self._data = data

    @property
    def cid(self):
        """
        Gets the cid of this ActionIn.
        Confirmation ID.

        :return: The cid of this ActionIn.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """
        Sets the cid of this ActionIn.
        Confirmation ID.

        :param cid: The cid of this ActionIn.
        :type: str
        """
        self._cid = cid

    @property
    def ddid(self):
        """
        Gets the ddid of this ActionIn.
        Destination Device ID.

        :return: The ddid of this ActionIn.
        :rtype: str
        """
        return self._ddid

    @ddid.setter
    def ddid(self, ddid):
        """
        Sets the ddid of this ActionIn.
        Destination Device ID.

        :param ddid: The ddid of this ActionIn.
        :type: str
        """
        self._ddid = ddid

    @property
    def sdid(self):
        """
        Gets the sdid of this ActionIn.
        Source Device ID.

        :return: The sdid of this ActionIn.
        :rtype: str
        """
        return self._sdid

    @sdid.setter
    def sdid(self, sdid):
        """
        Sets the sdid of this ActionIn.
        Source Device ID.

        :param sdid: The sdid of this ActionIn.
        :type: str
        """
        self._sdid = sdid

    @property
    def ts(self):
        """
        Gets the ts of this ActionIn.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :return: The ts of this ActionIn.
        :rtype: int
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """
        Sets the ts of this ActionIn.
        Timestamp (past, present or future). Defaults to current time if not provided.

        :param ts: The ts of this ActionIn.
        :type: int
        """
        self._ts = ts

    @property
    def type(self):
        """
        Gets the type of this ActionIn.
        Type.

        :return: The type of this ActionIn.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ActionIn.
        Type.

        :param type: The type of this ActionIn.
        :type: str
        """
        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
