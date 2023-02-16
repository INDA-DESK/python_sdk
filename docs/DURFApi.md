# inda_desk.DURFApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_durf_parser_post**](DURFApi.md#bulk_durf_parser_post) | **POST** /desk/v1/parse/durf/bulk/data/ | Bulk DURF Parser
[**durf_parser_post**](DURFApi.md#durf_parser_post) | **POST** /desk/v1/parse/durf/data/ | DURF Parser


# **bulk_durf_parser_post**
> ListPdfBase64DurfOutput bulk_durf_parser_post(listpdfbase64)

Bulk DURF Parser

 This method provides the information extraction from several DURF documents. The input should be a `zip` file containing only text-based `PDF` DURF. The zip file should be adequately encoded in `base64`. As optional field the client could add the file name.  Only text-based PDF DURF will be analyzed and the response provides the list of DURF adequately parsed with respectively name and a list of not parsable documents. Image-based PDF will not be analyzed and the response will be a not parsable document.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import durf_api
from inda_desk.model.listpdfbase64 import Listpdfbase64
from inda_desk.model.list_pdf_base64_durf_output import ListPdfBase64DurfOutput
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
    api_instance = durf_api.DURFApi(api_client)
    listpdfbase64 = Listpdfbase64(None) # Listpdfbase64 | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk DURF Parser
        api_response = api_instance.bulk_durf_parser_post(listpdfbase64)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling DURFApi->bulk_durf_parser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listpdfbase64** | [**Listpdfbase64**](Listpdfbase64.md)|  |

### Return type

[**ListPdfBase64DurfOutput**](ListPdfBase64DurfOutput.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Archive Successfully Parsed |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **durf_parser_post**
> OptionalDurfDoc durf_parser_post(pdfbase64)

DURF Parser

 This method provides the information extraction from single DURF document. The input document should be a text-based `PDF` DURF adequately encoded in `base64`. As optional field the client could add the file name. Image-based PDF will not be analyzed and the response will be a not parsable document.  If input is correctly provided, the response provides the information extraction from the DURF document. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import durf_api
from inda_desk.model.pdfbase64 import Pdfbase64
from inda_desk.model.optional_durf_doc import OptionalDurfDoc
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
    api_instance = durf_api.DURFApi(api_client)
    pdfbase64 = Pdfbase64(None) # Pdfbase64 | 

    # example passing only required values which don't have defaults set
    try:
        # DURF Parser
        api_response = api_instance.durf_parser_post(pdfbase64)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling DURFApi->durf_parser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdfbase64** | [**Pdfbase64**](Pdfbase64.md)|  |

### Return type

[**OptionalDurfDoc**](OptionalDurfDoc.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Successfully Parsed |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

