# inda_desk.VISURAApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_visura_parser_post**](VISURAApi.md#bulk_visura_parser_post) | **POST** /desk/v1/parse/visura/bulk/data/ | Bulk Visura Parser
[**visura_parser_post**](VISURAApi.md#visura_parser_post) | **POST** /desk/v1/parse/visura/data/ | Visura Parser


# **bulk_visura_parser_post**
> ListPdfBase64VisuraOutput bulk_visura_parser_post(listpdfbase64)

Bulk Visura Parser

 This method provides the information extraction from several *Visure Camerali* documents. The input should be a `zip` file containing only text-based `PDF` Visure Camerali. The zip file should be adequately encoded in `base64`. As optional field the client could add the file name.  Only text-based PDF Visure Camerali will be analyzed and the response provides the list of Visure Camerali adequately parsed with respectively name and a list of not parsable documents. Image-based PDF will not be analyzed and the response will be a not parsable document. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import visura_api
from inda_desk.model.listpdfbase64 import Listpdfbase64
from inda_desk.model.list_pdf_base64_visura_output import ListPdfBase64VisuraOutput
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
    api_instance = visura_api.VISURAApi(api_client)
    listpdfbase64 = Listpdfbase64(None) # Listpdfbase64 | 

    # example passing only required values which don't have defaults set
    try:
        # Bulk Visura Parser
        api_response = api_instance.bulk_visura_parser_post(listpdfbase64)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling VISURAApi->bulk_visura_parser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listpdfbase64** | [**Listpdfbase64**](Listpdfbase64.md)|  |

### Return type

[**ListPdfBase64VisuraOutput**](ListPdfBase64VisuraOutput.md)

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

# **visura_parser_post**
> OptionalVisuraDoc visura_parser_post(pdfbase64)

Visura Parser

 This method provides the information extraction from single *Visura Camerale* document. The input document should be a text-based `PDF` Visura Camerale adequately encoded in `base64`. As optional field the client could add the file name. Image-based PDF will not be analyzed and the response will be a not parsable document.  If input is correctly provided, the response provides the information extraction from the Visura Camerale document.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import visura_api
from inda_desk.model.optional_visura_doc import OptionalVisuraDoc
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
    api_instance = visura_api.VISURAApi(api_client)
    pdfbase64 = Pdfbase64(None) # Pdfbase64 | 

    # example passing only required values which don't have defaults set
    try:
        # Visura Parser
        api_response = api_instance.visura_parser_post(pdfbase64)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling VISURAApi->visura_parser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdfbase64** | [**Pdfbase64**](Pdfbase64.md)|  |

### Return type

[**OptionalVisuraDoc**](OptionalVisuraDoc.md)

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

