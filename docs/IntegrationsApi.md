# brainrex.IntegrationsApi

All URIs are relative to *https://api.bitlongs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crypto_get_candle_data**](IntegrationsApi.md#crypto_get_candle_data) | **POST** /crypto/get_candles | Downloads candle format market data
[**crypto_get_exchange_assets**](IntegrationsApi.md#crypto_get_exchange_assets) | **POST** /crypto/get_exchange_assets | Gets all currency pairs traded in selected exchange
[**crypto_get_orderbooks**](IntegrationsApi.md#crypto_get_orderbooks) | **POST** /crypto/get_orderbooks | Downloads candle format market data
[**crypto_get_supported_exchanges**](IntegrationsApi.md#crypto_get_supported_exchanges) | **GET** /crypto/get_supported_exchanges | Gets all cryptocurrency exchanges supported by the Brainrex API
[**crypto_get_ticker**](IntegrationsApi.md#crypto_get_ticker) | **POST** /crypto/get_ticker | Downloads candle format market data


# **crypto_get_candle_data**
> CandleResponse crypto_get_candle_data(text)

Downloads candle format market data

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import brainrex
from brainrex.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = brainrex.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = brainrex.IntegrationsApi(brainrex.ApiClient(configuration))
text = brainrex.Text() # Text | Exchange, trading pair and date rage for data

try:
    # Downloads candle format market data
    api_response = api_instance.crypto_get_candle_data(text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_candle_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**Text**](Text.md)| Exchange, trading pair and date rage for data | 

### Return type

[**CandleResponse**](CandleResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_exchange_assets**
> OHCLV crypto_get_exchange_assets(exchange_name)

Gets all currency pairs traded in selected exchange

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import brainrex
from brainrex.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = brainrex.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = brainrex.IntegrationsApi(brainrex.ApiClient(configuration))
exchange_name = brainrex.ExchangeName() # ExchangeName | Name of the cryptocurrency exchange

try:
    # Gets all currency pairs traded in selected exchange
    api_response = api_instance.crypto_get_exchange_assets(exchange_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_exchange_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_name** | [**ExchangeName**](ExchangeName.md)| Name of the cryptocurrency exchange | 

### Return type

[**OHCLV**](OHCLV.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_orderbooks**
> OHCLV crypto_get_orderbooks(text)

Downloads candle format market data

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import brainrex
from brainrex.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = brainrex.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = brainrex.IntegrationsApi(brainrex.ApiClient(configuration))
text = brainrex.Text1() # Text1 | Exchange, trading pair and date rage for data

try:
    # Downloads candle format market data
    api_response = api_instance.crypto_get_orderbooks(text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_orderbooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**Text1**](Text1.md)| Exchange, trading pair and date rage for data | 

### Return type

[**OHCLV**](OHCLV.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_supported_exchanges**
> crypto_get_supported_exchanges()

Gets all cryptocurrency exchanges supported by the Brainrex API

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import brainrex
from brainrex.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = brainrex.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = brainrex.IntegrationsApi(brainrex.ApiClient(configuration))

try:
    # Gets all cryptocurrency exchanges supported by the Brainrex API
    api_instance.crypto_get_supported_exchanges()
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_supported_exchanges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_get_ticker**
> OHCLV crypto_get_ticker(text)

Downloads candle format market data

Returns a list of candle data from specified market and data range

### Example
```python
from __future__ import print_function
import time
import brainrex
from brainrex.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = brainrex.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = brainrex.IntegrationsApi(brainrex.ApiClient(configuration))
text = brainrex.Text2() # Text2 | Get ticker data from specified crypto exchange

try:
    # Downloads candle format market data
    api_response = api_instance.crypto_get_ticker(text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->crypto_get_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**Text2**](Text2.md)| Get ticker data from specified crypto exchange | 

### Return type

[**OHCLV**](OHCLV.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

