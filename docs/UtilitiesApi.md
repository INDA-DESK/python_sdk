# inda_desk.UtilitiesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_status_get**](UtilitiesApi.md#health_status_get) | **GET** /desk/v1/ | Health Status


# **health_status_get**
> Check health_status_get()

Health Status

This method checks whether the service is up and running.  Returns the *status* of the service: <code style='color: #333333; opacity: 0.9'>green</code>, <code style='color: #333333; opacity: 0.9'>yellow</code> or <code style='color: #333333; opacity: 0.9'>red</code>.  A <code style='color: #333333; opacity: 0.9'>yellow</code> status means that at least the 80% of the services are available, <code style='color: #333333; opacity: 0.9'>red</code> that something is definitely not working properly.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import utilities_api
from inda_desk.model.http_validation_error import HTTPValidationError
from inda_desk.model.check import Check
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_desk.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_desk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_desk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = utilities_api.UtilitiesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health Status
        api_response = api_instance.health_status_get()
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling UtilitiesApi->health_status_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Check**](Check.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

