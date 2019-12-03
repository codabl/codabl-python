# brainrex.LanguageApi

All URIs are relative to *https://api.bitlongs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**language_get_crypto_entities**](LanguageApi.md#language_get_crypto_entities) | **POST** /entity/get_crypto_entities | Named Entity Recognition software capable of understanding cryptocurrency and blockchain speficic language.
[**language_get_general_sentiment**](LanguageApi.md#language_get_general_sentiment) | **POST** /sentiment/get_general_sentiment | Sentiment analysis score using a model trained for buy signals.
[**language_get_price_sentiment**](LanguageApi.md#language_get_price_sentiment) | **POST** /language/get_price_sentiment | Sentiment analysis score using a model trained for buy signals.


# **language_get_crypto_entities**
> language_get_crypto_entities(text)

Named Entity Recognition software capable of understanding cryptocurrency and blockchain speficic language.

Gives a 0 to 1 score, depending on buy/sell sentiment

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
api_instance = brainrex.LanguageApi(brainrex.ApiClient(configuration))
text = brainrex.Text5() # Text5 | String of text to be analyze for investor sentiment.

try:
    # Named Entity Recognition software capable of understanding cryptocurrency and blockchain speficic language.
    api_instance.language_get_crypto_entities(text)
except ApiException as e:
    print("Exception when calling LanguageApi->language_get_crypto_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**Text5**](Text5.md)| String of text to be analyze for investor sentiment. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_get_general_sentiment**
> str language_get_general_sentiment(text)

Sentiment analysis score using a model trained for buy signals.

Returns a -1 to 1 score, depending on positive/negative sentiment

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
api_instance = brainrex.LanguageApi(brainrex.ApiClient(configuration))
text = brainrex.Text3() # Text3 | String of text to be analyze for general sentiment.

try:
    # Sentiment analysis score using a model trained for buy signals.
    api_response = api_instance.language_get_general_sentiment(text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageApi->language_get_general_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**Text3**](Text3.md)| String of text to be analyze for general sentiment. | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_get_price_sentiment**
> str language_get_price_sentiment(text)

Sentiment analysis score using a model trained for buy signals.

Gives a 0 to 1 score, depending on buy/sell sentiment

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
api_instance = brainrex.LanguageApi(brainrex.ApiClient(configuration))
text = brainrex.Text4() # Text4 | String of text to be analyze for investor sentiment.

try:
    # Sentiment analysis score using a model trained for buy signals.
    api_response = api_instance.language_get_price_sentiment(text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageApi->language_get_price_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | [**Text4**](Text4.md)| String of text to be analyze for investor sentiment. | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

