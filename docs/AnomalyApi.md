# brainrex.AnomalyApi

All URIs are relative to *https://api.bitlongs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anomaly_batch**](AnomalyApi.md#anomaly_batch) | **POST** /anomaly/json/detect | Detects anomalies in historical data in batches. This endpoint uses your entire dataset as input


# **anomaly_batch**
> list[bool] anomaly_batch(request=request)

Detects anomalies in historical data in batches. This endpoint uses your entire dataset as input

The Anomaly Detect endpoint ingests time series data of all types, then monitors and detects abnormalities historical time series data. <br><br> Our AI selects from several models, choosing the one that fits the given data best, and we give you the avality to customize the sensitivy of the model. Our model has been trained to recognize anomalies in popular blockchain networks e.g. Bitcoin, Ethereum, learning from past events.

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
api_instance = brainrex.AnomalyApi(brainrex.ApiClient(configuration))
request = brainrex.TimeSeries() # TimeSeries | Time Series to be analyzed, with the following format. (optional)

try:
    # Detects anomalies in historical data in batches. This endpoint uses your entire dataset as input
    api_response = api_instance.anomaly_batch(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->anomaly_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**TimeSeries**](TimeSeries.md)| Time Series to be analyzed, with the following format. | [optional] 

### Return type

**list[bool]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

