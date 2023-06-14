# coding: utf-8

"""
    BrainRex API

    The Brainrex API is a collection of analytics tools and data integrations made for blockchain developers. In particular we offer Natural Language Processing and Anomaly detection algorithms that have been fine tune to understand text data and time series in the domain speficic setting of cryptocurrency and blockchain technology. This technology is intended to be use as building blocks to bigger applications, we offer examples on how to use them for Trading Backtesting and Smart Contract anomaly monitoring.  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.anomaly_api import AnomalyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAnomalyApi(unittest.TestCase):
    """AnomalyApi unit test stubs"""

    def setUp(self):
        self.api = AnomalyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_anomaly_batch(self):
        """Test case for anomaly_batch

        Detects anomalies in historical data in batches. This endpoint uses your entire dataset as input  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
