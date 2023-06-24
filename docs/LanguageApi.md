# brainrex.LanguageApi

All URIs are relative to *https://api.brainrex.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**language_get_crypto_entities**](LanguageApi.md#language_get_crypto_entities) | **POST** /entity/get_crypto_entities | Extracts known crypto entities like coin names, exchanges, media from text.
[**language_get_general_sentiment**](LanguageApi.md#language_get_general_sentiment) | **POST** /sentiment/get_general_sentiment | Returns a -1 to 1 score, depending on positive/negative sentiment
[**language_get_price_sentiment**](LanguageApi.md#language_get_price_sentiment) | **POST** /language/get_price_sentiment | Sentiment analysis score using a model trained for buy signals.

# **language_get_crypto_entities**
> language_get_crypto_entities(body)

Extracts known crypto entities like coin names, exchanges, media from text.

The Crypto Entities endpoint ingests written MIT Digital Currency Initiative Paper A paper describing how our sentiment and entity analyzer are built. And how the can be used for trading several cryptocurrencies successfully  We prove that using sentiment only as a input to a trading algorithm can be profitable. If combined with other machine learning models. This Paper could be published in MIT Crypto Economics Journal. <br><br> Our AI selects from several models, choosing the one that fits the given data best, and we give you the avality to customize the sensitivy of the model. Our model has been trained to recognize anomalies in popular blockchain networks e.g. Bitcoin, Ethereum, learning from past events.

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
body = brainrex.Text() # Text | String of text to be analyze for investor sentiment.

try:
    # Extracts known crypto entities like coin names, exchanges, media from text.
    api_instance.language_get_crypto_entities(body)
except ApiException as e:
    print("Exception when calling LanguageApi->language_get_crypto_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Text**](Text.md)| String of text to be analyze for investor sentiment. | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_get_general_sentiment**
> str language_get_general_sentiment(body)

Returns a -1 to 1 score, depending on positive/negative sentiment

This endpoints returns a score from -1 to +1 where depending on negative or positive attitude in the text.

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
body = brainrex.Text() # Text | String of text to be analyze for general sentiment.

try:
    # Returns a -1 to 1 score, depending on positive/negative sentiment
    api_response = api_instance.language_get_general_sentiment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageApi->language_get_general_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Text**](Text.md)| String of text to be analyze for general sentiment. | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **language_get_price_sentiment**
> str language_get_price_sentiment(body)

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
body = brainrex.Text() # Text | String of text to be analyze for investor sentiment.

try:
    # Sentiment analysis score using a model trained for buy signals.
    api_response = api_instance.language_get_price_sentiment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageApi->language_get_price_sentiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Text**](Text.md)| String of text to be analyze for investor sentiment. | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

