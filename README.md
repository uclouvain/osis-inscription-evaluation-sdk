# osis-inscription-evaluation-sdk
A set of API endpoints that allow you to enroll students to evaluations

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.5
- Package version: 1.5
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_inscription_evaluation_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_inscription_evaluation_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_inscription_evaluation_sdk
from pprint import pprint
from osis_inscription_evaluation_sdk.api import formulaire_api
from osis_inscription_evaluation_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_inscription_evaluation_sdk.model.choix_inscriptions_etudiant import ChoixInscriptionsEtudiant
from osis_inscription_evaluation_sdk.model.error import Error
from osis_inscription_evaluation_sdk.model.mon_formulaire_inscription_evaluations import MonFormulaireInscriptionEvaluations
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

    try:
        api_instance.enregistrer_formulaire(code_programme, choix_inscriptions_etudiant, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
    except osis_inscription_evaluation_sdk.ApiException as e:
        print("Exception when calling FormulaireApi->enregistrer_formulaire: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/inscription_aux_evaluations*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FormulaireApi* | [**enregistrer_formulaire**](docs/FormulaireApi.md#enregistrer_formulaire) | **POST** /{code_programme}/formulaire/ | 
*FormulaireApi* | [**get_formulaire_inscription**](docs/FormulaireApi.md#get_formulaire_inscription) | **GET** /{code_programme}/formulaire/ | 
*MesProgrammesApi* | [**liste_inscriptions_programmes**](docs/MesProgrammesApi.md#liste_inscriptions_programmes) | **GET** /mes_programmes/ | 
*RecapitulatifApi* | [**get_recapitulatif**](docs/RecapitulatifApi.md#get_recapitulatif) | **GET** /{code_programme}/recapitulatif/ | 
*RecapitulatifApi* | [**soumettre_formulaire**](docs/RecapitulatifApi.md#soumettre_formulaire) | **POST** /{code_programme}/recapitulatif/ | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [ChoixInscriptionsEtudiant](docs/ChoixInscriptionsEtudiant.md)
 - [ContactFaculte](docs/ContactFaculte.md)
 - [Error](docs/Error.md)
 - [Etudiant](docs/Etudiant.md)
 - [Formation](docs/Formation.md)
 - [InscriptionEvaluation](docs/InscriptionEvaluation.md)
 - [InscriptionFormation](docs/InscriptionFormation.md)
 - [MesFormations](docs/MesFormations.md)
 - [MonFormulaireInscriptionEvaluations](docs/MonFormulaireInscriptionEvaluations.md)
 - [MonFormulaireInscriptionEvaluationsInscriptions](docs/MonFormulaireInscriptionEvaluationsInscriptions.md)
 - [PeriodeInscription](docs/PeriodeInscription.md)
 - [Recapitulatif](docs/Recapitulatif.md)
 - [RecapitulatifInscriptions](docs/RecapitulatifInscriptions.md)
 - [RecapitulatifUniteEnseignement](docs/RecapitulatifUniteEnseignement.md)
 - [SessionDeTravail](docs/SessionDeTravail.md)
 - [TypeInscriptionEvaluationEnum](docs/TypeInscriptionEvaluationEnum.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_inscription_evaluation_sdk.apis and osis_inscription_evaluation_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_inscription_evaluation_sdk.api.default_api import DefaultApi`
- `from osis_inscription_evaluation_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.apis import *
from osis_inscription_evaluation_sdk.models import *
```

