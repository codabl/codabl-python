# coding: utf-8

"""
    Brainrex General Sentiment API

    Runs the price sentiment service of api.brainrex.com/sentiment/  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from brainrex.api_client import ApiClient


class LanguageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def language_get_crypto_entities(self, text, **kwargs):  # noqa: E501
        """Named Entity Recognition software capable of understanding cryptocurrency and blockchain speficic language.  # noqa: E501

        Gives a 0 to 1 score, depending on buy/sell sentiment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_get_crypto_entities(text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Text5 text: String of text to be analyze for investor sentiment. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.language_get_crypto_entities_with_http_info(text, **kwargs)  # noqa: E501
        else:
            (data) = self.language_get_crypto_entities_with_http_info(text, **kwargs)  # noqa: E501
            return data

    def language_get_crypto_entities_with_http_info(self, text, **kwargs):  # noqa: E501
        """Named Entity Recognition software capable of understanding cryptocurrency and blockchain speficic language.  # noqa: E501

        Gives a 0 to 1 score, depending on buy/sell sentiment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_get_crypto_entities_with_http_info(text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Text5 text: String of text to be analyze for investor sentiment. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method language_get_crypto_entities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `language_get_crypto_entities`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'text' in params:
            body_params = params['text']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/entity/get_crypto_entities', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def language_get_general_sentiment(self, text, **kwargs):  # noqa: E501
        """Sentiment analysis score using a model trained for buy signals.  # noqa: E501

        Returns a -1 to 1 score, depending on positive/negative sentiment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_get_general_sentiment(text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Text3 text: String of text to be analyze for general sentiment. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.language_get_general_sentiment_with_http_info(text, **kwargs)  # noqa: E501
        else:
            (data) = self.language_get_general_sentiment_with_http_info(text, **kwargs)  # noqa: E501
            return data

    def language_get_general_sentiment_with_http_info(self, text, **kwargs):  # noqa: E501
        """Sentiment analysis score using a model trained for buy signals.  # noqa: E501

        Returns a -1 to 1 score, depending on positive/negative sentiment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_get_general_sentiment_with_http_info(text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Text3 text: String of text to be analyze for general sentiment. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method language_get_general_sentiment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `language_get_general_sentiment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'text' in params:
            body_params = params['text']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/sentiment/get_general_sentiment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def language_get_price_sentiment(self, text, **kwargs):  # noqa: E501
        """Sentiment analysis score using a model trained for buy signals.  # noqa: E501

        Gives a 0 to 1 score, depending on buy/sell sentiment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_get_price_sentiment(text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Text4 text: String of text to be analyze for investor sentiment. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.language_get_price_sentiment_with_http_info(text, **kwargs)  # noqa: E501
        else:
            (data) = self.language_get_price_sentiment_with_http_info(text, **kwargs)  # noqa: E501
            return data

    def language_get_price_sentiment_with_http_info(self, text, **kwargs):  # noqa: E501
        """Sentiment analysis score using a model trained for buy signals.  # noqa: E501

        Gives a 0 to 1 score, depending on buy/sell sentiment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.language_get_price_sentiment_with_http_info(text, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Text4 text: String of text to be analyze for investor sentiment. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method language_get_price_sentiment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params or
                params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `language_get_price_sentiment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'text' in params:
            body_params = params['text']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/language/get_price_sentiment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)