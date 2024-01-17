# osis_inscription_evaluation_sdk.RecapitulatifApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/inscription_evaluation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recapitulatif**](RecapitulatifApi.md#get_recapitulatif) | **GET** /{code_programme}/recapitulatif/ | 
[**soumettre_formulaire**](RecapitulatifApi.md#soumettre_formulaire) | **POST** /{code_programme}/recapitulatif/ | 


# **get_recapitulatif**
> Recapitulatif get_recapitulatif(code_programme)



Renvoie le récapitulatif des inscriptions aux évaluations de l'utilisateur (étudiant) pour l'année en cours

### Example

* Api Key Authentication (Token):

```python
import time
import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.api import recapitulatif_api
from osis_inscription_evaluation_sdk.model.recapitulatif import Recapitulatif
from osis_inscription_evaluation_sdk.model.error import Error
from osis_inscription_evaluation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/inscription_evaluation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_inscription_evaluation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/inscription_evaluation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_inscription_evaluation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recapitulatif_api.RecapitulatifApi(api_client)
    code_programme = "LDROI100B" # str | Le code du programme auquel est inscrit l'étudiant
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_recapitulatif(code_programme)
        pprint(api_response)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling RecapitulatifApi->get_recapitulatif: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_recapitulatif(code_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling RecapitulatifApi->get_recapitulatif: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_programme** | **str**| Le code du programme auquel est inscrit l&#39;étudiant |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**Recapitulatif**](Recapitulatif.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soumettre_formulaire**
> soumettre_formulaire(code_programme)



Soumet définitivement le formulaire d'inscription de l'étudiant

### Example

* Api Key Authentication (Token):

```python
import time
import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.api import recapitulatif_api
from osis_inscription_evaluation_sdk.model.error import Error
from osis_inscription_evaluation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/inscription_evaluation
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_inscription_evaluation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/inscription_evaluation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_inscription_evaluation_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recapitulatif_api.RecapitulatifApi(api_client)
    code_programme = "LDROI100B" # str | Le code du programme auquel est inscrit l'étudiant
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.soumettre_formulaire(code_programme)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling RecapitulatifApi->soumettre_formulaire: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.soumettre_formulaire(code_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling RecapitulatifApi->soumettre_formulaire: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_programme** | **str**| Le code du programme auquel est inscrit l&#39;étudiant |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Requested |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

