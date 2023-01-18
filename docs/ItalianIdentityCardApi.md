# inda_desk.ItalianIdentityCardApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**italian_id_card_electronic_version_post**](ItalianIdentityCardApi.md#italian_id_card_electronic_version_post) | **POST** /desk/v1/parsing/id-docs/italian/identity-card/electronic/ | Italian ID Card - Electronic Version
[**italian_id_card_paper_version_post**](ItalianIdentityCardApi.md#italian_id_card_paper_version_post) | **POST** /desk/v1/parsing/id-docs/italian/identity-card/paper/ | Italian ID Card - Paper Version


# **italian_id_card_electronic_version_post**
> CINParsingResponse italian_id_card_electronic_version_post(request)

Italian ID Card - Electronic Version

 This method provides the information extraction from the Italian [*Carta di identità elettronica*](https://en.wikipedia.org/wiki/Italian_electronic_identity_card) (also known as *Electronic Identity Card*), which is a document used to prove a person's identity. It contains several information about its holder, such as their name and surname, their nationality and so on.  Starting from a scanned document (sent through the request field *File* after a <code style='color: #333333; opacity: 0.9'>base64</code> encoding), this  function performs several operations aimed at retrieving the main information contained in the identity card.  The input file size should not exceed 6 MB.  Allowed file extensions are: <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code>.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import italian_identity_card_api
from inda_desk.model.request import Request
from inda_desk.model.cin_parsing_response import CINParsingResponse
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
    api_instance = italian_identity_card_api.ItalianIdentityCardApi(api_client)
    request = Request(None) # Request | 

    # example passing only required values which don't have defaults set
    try:
        # Italian ID Card - Electronic Version
        api_response = api_instance.italian_id_card_electronic_version_post(request)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling ItalianIdentityCardApi->italian_id_card_electronic_version_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  |

### Return type

[**CINParsingResponse**](CINParsingResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Parsed ID Document |  -  |
**422** | Unprocessable Entity |  -  |
**415** | Unsupported Media Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **italian_id_card_paper_version_post**
> CIVParsingResponse italian_id_card_paper_version_post(request)

Italian ID Card - Paper Version

 This method provides the information extraction from the Italian  [*Carta di identità cartacea*](https://it.wikipedia.org/wiki/Carta_d%27identit%C3%A0_cartacea_italiana), which is a  document used to prove a person's identity. It contains several information about its holder, such as their name and surname, their nationality and so on, along  with some of their physical aspects, like their height.  Starting from a scanned document (sent through the request field *File* after a <code style='color: #333333; opacity: 0.9'>base64</code> encoding), this  function performs several operations aimed at retrieving the main information contained in the identity card.  The input file size should not exceed 6 MB.  Allowed file extensions are: <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code>.  Please note that this method is meant to parse the so-called *paper version* of this document; nowadays, it is  replaced by its digital version, whose parsing is available at  [Italian ID Card - Electronic Version](https:///desk/docs/v1/#operation/cin_parsing_desk_v1_parsing_id_docs_italian_identity_card_electronic__post).  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import italian_identity_card_api
from inda_desk.model.civ_parsing_response import CIVParsingResponse
from inda_desk.model.request import Request
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
    api_instance = italian_identity_card_api.ItalianIdentityCardApi(api_client)
    request = Request(None) # Request | 

    # example passing only required values which don't have defaults set
    try:
        # Italian ID Card - Paper Version
        api_response = api_instance.italian_id_card_paper_version_post(request)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling ItalianIdentityCardApi->italian_id_card_paper_version_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  |

### Return type

[**CIVParsingResponse**](CIVParsingResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Parsed ID Document |  -  |
**422** | Unprocessable Entity |  -  |
**415** | Unsupported Media Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

