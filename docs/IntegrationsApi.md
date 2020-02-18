# codabl.IntegrationsApi

All URIs are relative to *https://api.bitlongs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crypto_get_candle_data**](IntegrationsApi.md#crypto_get_candle_data) | **POST** /crypto/get_candles | Downloads candle format market data
[**crypto_get_exchange_assets**](IntegrationsApi.md#crypto_get_exchange_assets) | **POST** /crypto/get_exchange_assets | Gets all coin pairs traded in specified exchange
[**crypto_get_orderbooks**](IntegrationsApi.md#crypto_get_orderbooks) | **POST** /crypto/get_orderbooks | Returns the current state of the orderbook.
[**crypto_get_supported_exchanges**](IntegrationsApi.md#crypto_get_supported_exchanges) | **GET** /crypto/get_supported_exchanges | Gets all cryptocurrency exchanges supported by the Codabl API
[**crypto_get_ticker**](IntegrationsApi.md#crypto_get_ticker) | **POST** /crypto/get_ticker | Downloads candle format market data


# **crypto_get_candle_data**
> CandleResponse crypto_get_candle_data(candle_request)

Downloads candle format market data

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import codabl
from codabl.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = codabl.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = codabl.IntegrationsApi(codabl.ApiClient(configuration))
candle_request = codabl.CandleRequest() # CandleRequest | The Get candles end point return market data in Open High Close Volume format. In order to use this endpoint you need to enter your API keys to your data provider in the console

try:
    # Downloads candle format market data
    api_response = api_instance.crypto_get_candle_data(candle_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_candle_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candle_request** | [**CandleRequest**](CandleRequest.md)| The Get candles end point return market data in Open High Close Volume format. In order to use this endpoint you need to enter your API keys to your data provider in the console | 

### Return type

[**CandleResponse**](CandleResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_exchange_assets**
> ExchangeAssetsResponse crypto_get_exchange_assets(exchange)

Gets all coin pairs traded in specified exchange

This endpoint returns all the Available currency pairs

### Example
```python
from __future__ import print_function
import time
import codabl
from codabl.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = codabl.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = codabl.IntegrationsApi(codabl.ApiClient(configuration))
exchange = codabl.Exchange() # Exchange | Name of the cryptocurrency exchange

try:
    # Gets all coin pairs traded in specified exchange
    api_response = api_instance.crypto_get_exchange_assets(exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_exchange_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | [**Exchange**](Exchange.md)| Name of the cryptocurrency exchange | 

### Return type

[**ExchangeAssetsResponse**](ExchangeAssetsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_orderbooks**
> OrderbookResponse crypto_get_orderbooks(orderbook_request)

Returns the current state of the orderbook.

This endpoint returns the current state of the ordebook with a limit set by you. The maximun orderbook depth is 25.

### Example
```python
from __future__ import print_function
import time
import codabl
from codabl.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = codabl.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = codabl.IntegrationsApi(codabl.ApiClient(configuration))
orderbook_request = codabl.OrderbookRequest() # OrderbookRequest | Exchange, trading pair and date rage for data

try:
    # Returns the current state of the orderbook.
    api_response = api_instance.crypto_get_orderbooks(orderbook_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_orderbooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderbook_request** | [**OrderbookRequest**](OrderbookRequest.md)| Exchange, trading pair and date rage for data | 

### Return type

[**OrderbookResponse**](OrderbookResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_supported_exchanges**
> SupportedExchanges crypto_get_supported_exchanges()

Gets all cryptocurrency exchanges supported by the Codabl API

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import codabl
from codabl.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = codabl.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = codabl.IntegrationsApi(codabl.ApiClient(configuration))

try:
    # Gets all cryptocurrency exchanges supported by the Codabl API
    api_response = api_instance.crypto_get_supported_exchanges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_supported_exchanges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedExchanges**](SupportedExchanges.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_ticker**
> TickerResponse crypto_get_ticker(exchange)

Downloads candle format market data

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import codabl
from codabl.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = codabl.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = codabl.IntegrationsApi(codabl.ApiClient(configuration))
exchange = codabl.Exchange() # Exchange | Get ticker data from specified crypto exchange

try:
    # Downloads candle format market data
    api_response = api_instance.crypto_get_ticker(exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | [**Exchange**](Exchange.md)| Get ticker data from specified crypto exchange | 

### Return type

[**TickerResponse**](TickerResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

