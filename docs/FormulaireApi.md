# osis_inscription_evaluation_sdk.FormulaireApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enregistrer_formulaire**](FormulaireApi.md#enregistrer_formulaire) | **POST** /{code_programme}/formulaire/ | 
[**get_formulaire_inscription**](FormulaireApi.md#get_formulaire_inscription) | **GET** /{code_programme}/formulaire/ | 
[**marquer_formulaire_inscription_eval_comme_lu**](FormulaireApi.md#marquer_formulaire_inscription_eval_comme_lu) | **POST** /{code_programme}/formulaire/marquer_lu/ | 


# **enregistrer_formulaire**
> enregistrer_formulaire(code_programme, choix_inscriptions_etudiant)



Enregistre les choix d'inscriptions aux évaluations de l'étudiant

### Example

* Api Key Authentication (Token):

```python
import time
import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.api import formulaire_api
from osis_inscription_evaluation_sdk.model.error import Error
from osis_inscription_evaluation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_inscription_evaluation_sdk.model.choix_inscriptions_etudiant import ChoixInscriptionsEtudiant
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_inscription_evaluation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations"
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
    api_instance = formulaire_api.FormulaireApi(api_client)
    code_programme = "LDROI100B" # str | Le code du programme auquel est inscrit l'étudiant
    choix_inscriptions_etudiant = ChoixInscriptionsEtudiant(
        demandes_inscription=[
            "LDROI1001",
        ],
        demandes_desinscription=[
            "LDROI1002",
        ],
    ) # ChoixInscriptionsEtudiant | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.enregistrer_formulaire(code_programme, choix_inscriptions_etudiant)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling FormulaireApi->enregistrer_formulaire: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.enregistrer_formulaire(code_programme, choix_inscriptions_etudiant, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling FormulaireApi->enregistrer_formulaire: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_programme** | **str**| Le code du programme auquel est inscrit l&#39;étudiant |
 **choix_inscriptions_etudiant** | [**ChoixInscriptionsEtudiant**](ChoixInscriptionsEtudiant.md)|  |
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Requested |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_formulaire_inscription**
> MonFormulaireInscriptionEvaluations get_formulaire_inscription(code_programme)



Renvoie les inscriptions aux évaluations de l'utilisateur (étudiant) pour l'année en cours

### Example

* Api Key Authentication (Token):

```python
import time
import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.api import formulaire_api
from osis_inscription_evaluation_sdk.model.mon_formulaire_inscription_evaluations import MonFormulaireInscriptionEvaluations
from osis_inscription_evaluation_sdk.model.error import Error
from osis_inscription_evaluation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_inscription_evaluation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations"
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
    api_instance = formulaire_api.FormulaireApi(api_client)
    code_programme = "LDROI100B" # str | Le code du programme auquel est inscrit l'étudiant
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_formulaire_inscription(code_programme)
        pprint(api_response)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling FormulaireApi->get_formulaire_inscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_formulaire_inscription(code_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling FormulaireApi->get_formulaire_inscription: %s\n" % e)
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

[**MonFormulaireInscriptionEvaluations**](MonFormulaireInscriptionEvaluations.md)

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

# **marquer_formulaire_inscription_eval_comme_lu**
> marquer_formulaire_inscription_eval_comme_lu(code_programme)



Marque le formulaire d'inscription comme lu par l'étudiant

### Example

* Api Key Authentication (Token):

```python
import time
import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.api import formulaire_api
from osis_inscription_evaluation_sdk.model.error import Error
from osis_inscription_evaluation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_inscription_evaluation_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations"
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
    api_instance = formulaire_api.FormulaireApi(api_client)
    code_programme = "LDROI100B" # str | Le code du programme auquel est inscrit l'étudiant
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.marquer_formulaire_inscription_eval_comme_lu(code_programme)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling FormulaireApi->marquer_formulaire_inscription_eval_comme_lu: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.marquer_formulaire_inscription_eval_comme_lu(code_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling FormulaireApi->marquer_formulaire_inscription_eval_comme_lu: %s\n" % e)
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

