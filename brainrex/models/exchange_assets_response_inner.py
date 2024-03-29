# coding: utf-8

"""
    Brainrex API

    The Brainrex API is a collection of analytics tools and data integrations made for blockchain developers. In particular we offer Natural Language Processing and Anomaly detection algorithms that have been fine tune to understand text data and time series in the domain speficic setting of cryptocurrency and blockchain technology.  # noqa: E501

    OpenAPI spec version: 1.0.3-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExchangeAssetsResponseInner(object):
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
        'id': 'float',
        'tradin_sym': 'str',
        'symbol': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'tradin_sym': 'tradinSym',
        'symbol': 'symbol'
    }

    def __init__(self, name=None, id=None, tradin_sym=None, symbol=None):  # noqa: E501
        """ExchangeAssetsResponseInner - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._tradin_sym = None
        self._symbol = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if tradin_sym is not None:
            self.tradin_sym = tradin_sym
        if symbol is not None:
            self.symbol = symbol

    @property
    def name(self):
        """Gets the name of this ExchangeAssetsResponseInner.  # noqa: E501

        Highest price of the time frame with two decimal points  # noqa: E501

        :return: The name of this ExchangeAssetsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExchangeAssetsResponseInner.

        Highest price of the time frame with two decimal points  # noqa: E501

        :param name: The name of this ExchangeAssetsResponseInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this ExchangeAssetsResponseInner.  # noqa: E501

        Percetange change in the last 24 hours  # noqa: E501

        :return: The id of this ExchangeAssetsResponseInner.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExchangeAssetsResponseInner.

        Percetange change in the last 24 hours  # noqa: E501

        :param id: The id of this ExchangeAssetsResponseInner.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def tradin_sym(self):
        """Gets the tradin_sym of this ExchangeAssetsResponseInner.  # noqa: E501

        Volume of currency exchanged in the time frame with two decimal points  # noqa: E501

        :return: The tradin_sym of this ExchangeAssetsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._tradin_sym

    @tradin_sym.setter
    def tradin_sym(self, tradin_sym):
        """Sets the tradin_sym of this ExchangeAssetsResponseInner.

        Volume of currency exchanged in the time frame with two decimal points  # noqa: E501

        :param tradin_sym: The tradin_sym of this ExchangeAssetsResponseInner.  # noqa: E501
        :type: str
        """

        self._tradin_sym = tradin_sym

    @property
    def symbol(self):
        """Gets the symbol of this ExchangeAssetsResponseInner.  # noqa: E501

        Volume of currency exchanged in the time frame with two decimal points  # noqa: E501

        :return: The symbol of this ExchangeAssetsResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this ExchangeAssetsResponseInner.

        Volume of currency exchanged in the time frame with two decimal points  # noqa: E501

        :param symbol: The symbol of this ExchangeAssetsResponseInner.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

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
        if issubclass(ExchangeAssetsResponseInner, dict):
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
        if not isinstance(other, ExchangeAssetsResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
