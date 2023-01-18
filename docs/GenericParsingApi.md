# inda_desk.GenericParsingApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generic_parser_post**](GenericParsingApi.md#generic_parser_post) | **POST** /desk/v1/parsing/text/ | Generic Parser


# **generic_parser_post**
> TextResponse generic_parser_post(doc)

Generic Parser

 This method extracts the text from a document. In particular, the method requires in input the *binary* and the *extension* of the file and automatically performs (*i*) Document Layout Analysis, (*ii*) Optical Character Recognition (if the input document is an image), and (*iii*) Text Extraction.  The allowed file extensions are *pdf*, *doc*, *docx*, *odt*, *txt*, *html*, *pptx*, *rtf*, *jpeg*, *png*, *jpg*, *tif*, *tiff*. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_desk
from inda_desk.api import generic_parsing_api
from inda_desk.model.doc import Doc
from inda_desk.model.text_response import TextResponse
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
    api_instance = generic_parsing_api.GenericParsingApi(api_client)
    doc = Doc(None) # Doc | 
    lang = "lang_example" # str | Language model to use to interpretate the text, default is italian. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generic Parser
        api_response = api_instance.generic_parser_post(doc)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling GenericParsingApi->generic_parser_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generic Parser
        api_response = api_instance.generic_parser_post(doc, lang=lang)
        pprint(api_response)
    except inda_desk.ApiException as e:
        print("Exception when calling GenericParsingApi->generic_parser_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc** | [**Doc**](Doc.md)|  |
 **lang** | **str**| Language model to use to interpretate the text, default is italian. | [optional]

### Return type

[**TextResponse**](TextResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Parsed Text |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

