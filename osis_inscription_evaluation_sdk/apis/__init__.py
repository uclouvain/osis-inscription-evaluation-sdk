
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.formulaire_api import FormulaireApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_inscription_evaluation_sdk.api.formulaire_api import FormulaireApi
from osis_inscription_evaluation_sdk.api.mes_programmes_api import MesProgrammesApi
from osis_inscription_evaluation_sdk.api.recapitulatif_api import RecapitulatifApi
