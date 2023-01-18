# inda_desk.DURCApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_durc_parser_post**](DURCApi.md#bulk_durc_parser_post) | **POST** /desk/v1/parsing/bulk/durc/ | Bulk DURC Parser
[**durc_parser_post**](DURCApi.md#durc_parser_post) | **POST** /desk/v1/parsing/durc/ | DURC Parser


# **bulk_durc_parser_post**
> ListPdfBase64DurcOutput bulk_durc_parser_post(listpdfbase64)

Bulk DURC Parser

 This method provides the information extraction from several DURC documents. The input should be a `zip` file containing only text-based `PDF` DURC. The zip file should be adequately encoded in `base64`. As optional field the client could add the file name.  Only text-based PDF DURC will be analyzed and the response provides the list of DURC adequately parsed and a list of not pasable documents. Image-based PDF will not be analyzed and the response will be a not parsable document. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import durc_api
from inda_desk.model.listpdfbase64 import Listpdfbase64
from inda_desk.model.list_pdf_base64_durc_output import ListPdfBase64DurcOutput
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
    api_instance = durc_api.DURCApi(api_client)
    listpdfbase64 = Listpdfbase64(None) # Listpdfbase64 | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk DURC Parser
        api_response = api_instance.bulk_durc_parser_post(listpdfbase64)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling DURCApi->bulk_durc_parser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listpdfbase64** | [**Listpdfbase64**](Listpdfbase64.md)|  |

### Return type

[**ListPdfBase64DurcOutput**](ListPdfBase64DurcOutput.md)

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

# **durc_parser_post**
> OptionalDurcDoc durc_parser_post(pdfbase64)

DURC Parser

 This method provides the information extraction from single DURC document. The input document should be a text-based `PDF` DURC adequately encoded in `base64`. As optional field the client could add the file name. Image-based PDF will not be analyzed and the response will be a not parsable document.  If input is correctly provided, the response provides the information extraction from the DURC document. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import durc_api
from inda_desk.model.optional_durc_doc import OptionalDurcDoc
from inda_desk.model.pdfbase64 import Pdfbase64
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
    api_instance = durc_api.DURCApi(api_client)
    pdfbase64 = Pdfbase64(None) # Pdfbase64 | 

    # example passing only required values which don't have defaults set
    try:
        # DURC Parser
        api_response = api_instance.durc_parser_post(pdfbase64)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling DURCApi->durc_parser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdfbase64** | [**Pdfbase64**](Pdfbase64.md)|  |

### Return type

[**OptionalDurcDoc**](OptionalDurcDoc.md)

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

