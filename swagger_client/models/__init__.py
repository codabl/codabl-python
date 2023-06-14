# coding: utf-8

# flake8: noqa
"""
    BrainRex API

    The Brainrex API is a collection of analytics tools and data integrations made for blockchain developers. In particular we offer Natural Language Processing and Anomaly detection algorithms that have been fine tune to understand text data and time series in the domain speficic setting of cryptocurrency and blockchain technology. This technology is intended to be use as building blocks to bigger applications, we offer examples on how to use them for Trading Backtesting and Smart Contract anomaly monitoring.  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.candle_request import CandleRequest
from swagger_client.models.candle_response import CandleResponse
from swagger_client.models.error import Error
from swagger_client.models.exchange import Exchange
from swagger_client.models.exchange_assets_response import ExchangeAssetsResponse
from swagger_client.models.exchange_assets_response_inner import ExchangeAssetsResponseInner
from swagger_client.models.ohclv import OHCLV
from swagger_client.models.orderbook_request import OrderbookRequest
from swagger_client.models.orderbook_response import OrderbookResponse
from swagger_client.models.point_time_series import PointTimeSeries
from swagger_client.models.supported_exchanges import SupportedExchanges
from swagger_client.models.text import Text
from swagger_client.models.ticker_response import TickerResponse
from swagger_client.models.ticker_response_inner import TickerResponseInner
from swagger_client.models.time_series import TimeSeries