"""
    INDA DESK - INtelligent Data Analysis for document parsing

     # Introduction  **INDA (INtelligent Data Analysis)** is an [Intervieweb](https://www.intervieweb.it/hrm/)  AI solution provided as a RESTful API.  The INDA pricing model is *credits-based*, which means that a certain number of credits is associated to each API request. Hence, users have to purchase a certain amount of credits (established according to their needs) which will be reduced  at each API call. INDA accepts and processes a user's request only if their credits quota is greater than - or,  at least, equal to - the number of credits required by that request. To obtain further details on the pricing, please visit our [site](https://inda.ai) or contact us.   Financial documents, invoices, taxes, and certifications are common documents  normally stored as Portable Document Format (PDF). Often such documents are used as financial approval or as input for next bureaucratic steps. These operations are commonly made by human beings where they should read the documents and make decision based on the information inside the document.      INDA DESK was born to automatize the operations of information extraction from commonly used financial documents  such as *single document of contribution regularity* (DURC), *single document of fiscal regularity* (DURF) or *visure camerali*.  The automatization provides scalability and the speeding up of the processes related with such documents.   The following documentation is addressed both to developers, in order to provide all technical details for INDA integration, and to managers, to guide them in the exploration of the implementation possibilities.  The host of the API is <span style=\"color:blue\">https<area>://api.inda.ai/desk/v1/</span>. We recommend to check the API version and build (displayed near the documentation title). You can contact us at support@intervieweb.it in case of problems, suggestions, or particular needs.  The search panel on the left can be used to navigate through the documentation and provides an overview of the API structure. On the right, you can find (*i*) the url of the method, (*ii*) an example of request body (if present), and (*iii*) an example of response for each response code. Finally, in the central section of each API method, you can find (*i*) a general description of the purpose of the method, (*ii*) details on parameters and request body schema (if present), and (*iii*) details on response schema, error models, and error codes.    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@intervieweb.it
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from inda_desk.api_client import ApiClient, Endpoint as _Endpoint
from inda_desk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from inda_desk.model.cin_parsing_response import CINParsingResponse
from inda_desk.model.civ_parsing_response import CIVParsingResponse
from inda_desk.model.request import Request


class ItalianIdentityCardApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.italian_id_card_electronic_version_post_endpoint = _Endpoint(
            settings={
                'response_type': (CINParsingResponse,),
                'auth': [
                    'APIKey'
                ],
                'endpoint_path': '/desk/v1/parsing/id-docs/italian/identity-card/electronic/',
                'operation_id': 'italian_id_card_electronic_version_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'request',
                ],
                'required': [
                    'request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'request':
                        (Request,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.italian_id_card_paper_version_post_endpoint = _Endpoint(
            settings={
                'response_type': (CIVParsingResponse,),
                'auth': [
                    'APIKey'
                ],
                'endpoint_path': '/desk/v1/parsing/id-docs/italian/identity-card/paper/',
                'operation_id': 'italian_id_card_paper_version_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'request',
                ],
                'required': [
                    'request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'request':
                        (Request,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def italian_id_card_electronic_version_post(
        self,
        request,
        **kwargs
    ):
        """Italian ID Card - Electronic Version  # noqa: E501

         This method provides the information extraction from the Italian [*Carta di identità elettronica*](https://en.wikipedia.org/wiki/Italian_electronic_identity_card) (also known as *Electronic Identity Card*), which is a document used to prove a person's identity. It contains several information about its holder, such as their name and surname, their nationality and so on.  Starting from a scanned document (sent through the request field *File* after a <code style='color: #333333; opacity: 0.9'>base64</code> encoding), this  function performs several operations aimed at retrieving the main information contained in the identity card.  The input file size should not exceed 6 MB.  Allowed file extensions are: <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code>.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.italian_id_card_electronic_version_post(request, async_req=True)
        >>> result = thread.get()

        Args:
            request (Request):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CINParsingResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['request'] = \
            request
        return self.italian_id_card_electronic_version_post_endpoint.call_with_http_info(**kwargs)

    def italian_id_card_paper_version_post(
        self,
        request,
        **kwargs
    ):
        """Italian ID Card - Paper Version  # noqa: E501

         This method provides the information extraction from the Italian  [*Carta di identità cartacea*](https://it.wikipedia.org/wiki/Carta_d%27identit%C3%A0_cartacea_italiana), which is a  document used to prove a person's identity. It contains several information about its holder, such as their name and surname, their nationality and so on, along  with some of their physical aspects, like their height.  Starting from a scanned document (sent through the request field *File* after a <code style='color: #333333; opacity: 0.9'>base64</code> encoding), this  function performs several operations aimed at retrieving the main information contained in the identity card.  The input file size should not exceed 6 MB.  Allowed file extensions are: <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code>.  Please note that this method is meant to parse the so-called *paper version* of this document; nowadays, it is  replaced by its digital version, whose parsing is available at  [Italian ID Card - Electronic Version](https:///desk/docs/v1/#operation/cin_parsing_desk_v1_parsing_id_docs_italian_identity_card_electronic__post).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.italian_id_card_paper_version_post(request, async_req=True)
        >>> result = thread.get()

        Args:
            request (Request):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CIVParsingResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['request'] = \
            request
        return self.italian_id_card_paper_version_post_endpoint.call_with_http_info(**kwargs)

