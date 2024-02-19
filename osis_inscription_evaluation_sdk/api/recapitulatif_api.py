"""
    Evaluation enrollments service

    A set of API endpoints that allow you to enroll students to evaluations  # noqa: E501

    The version of the OpenAPI document: 1.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_inscription_evaluation_sdk.api_client import ApiClient, Endpoint as _Endpoint
from osis_inscription_evaluation_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from osis_inscription_evaluation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_inscription_evaluation_sdk.model.error import Error
from osis_inscription_evaluation_sdk.model.recapitulatif import Recapitulatif


class RecapitulatifApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_recapitulatif_endpoint = _Endpoint(
            settings={
                'response_type': (Recapitulatif,),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/{code_programme}/recapitulatif/',
                'operation_id': 'get_recapitulatif',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'code_programme',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'code_programme',
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
                    'code_programme':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'code_programme': 'code_programme',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'code_programme': 'path',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.soumettre_formulaire_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/{code_programme}/recapitulatif/',
                'operation_id': 'soumettre_formulaire',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'code_programme',
                    'accept_language',
                    'x_user_first_name',
                    'x_user_last_name',
                    'x_user_email',
                    'x_user_global_id',
                ],
                'required': [
                    'code_programme',
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
                    'code_programme':
                        (str,),
                    'accept_language':
                        (AcceptedLanguageEnum,),
                    'x_user_first_name':
                        (str,),
                    'x_user_last_name':
                        (str,),
                    'x_user_email':
                        (str,),
                    'x_user_global_id':
                        (str,),
                },
                'attribute_map': {
                    'code_programme': 'code_programme',
                    'accept_language': 'Accept-Language',
                    'x_user_first_name': 'X-User-FirstName',
                    'x_user_last_name': 'X-User-LastName',
                    'x_user_email': 'X-User-Email',
                    'x_user_global_id': 'X-User-GlobalID',
                },
                'location_map': {
                    'code_programme': 'path',
                    'accept_language': 'header',
                    'x_user_first_name': 'header',
                    'x_user_last_name': 'header',
                    'x_user_email': 'header',
                    'x_user_global_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_recapitulatif(
        self,
        code_programme,
        **kwargs
    ):
        """get_recapitulatif  # noqa: E501

        Renvoie le récapitulatif des inscriptions aux évaluations de l'utilisateur (étudiant) pour l'année en cours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_recapitulatif(code_programme, async_req=True)
        >>> result = thread.get()

        Args:
            code_programme (str): Le code du programme auquel est inscrit l'étudiant

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
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
            async_req (bool): execute request asynchronously

        Returns:
            Recapitulatif
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
        kwargs['code_programme'] = \
            code_programme
        return self.get_recapitulatif_endpoint.call_with_http_info(**kwargs)

    def soumettre_formulaire(
        self,
        code_programme,
        **kwargs
    ):
        """soumettre_formulaire  # noqa: E501

        Soumet définitivement le formulaire d'inscription de l'étudiant  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.soumettre_formulaire(code_programme, async_req=True)
        >>> result = thread.get()

        Args:
            code_programme (str): Le code du programme auquel est inscrit l'étudiant

        Keyword Args:
            accept_language (AcceptedLanguageEnum): The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.) . [optional]
            x_user_first_name (str): [optional]
            x_user_last_name (str): [optional]
            x_user_email (str): [optional]
            x_user_global_id (str): [optional]
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
            async_req (bool): execute request asynchronously

        Returns:
            None
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
        kwargs['code_programme'] = \
            code_programme
        return self.soumettre_formulaire_endpoint.call_with_http_info(**kwargs)

