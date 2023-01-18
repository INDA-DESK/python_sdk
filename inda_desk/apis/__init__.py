
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from inda_desk.api.authentication_api import AuthenticationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from inda_desk.api.authentication_api import AuthenticationApi
from inda_desk.api.credits_management_api import CreditsManagementApi
from inda_desk.api.durc_api import DURCApi
from inda_desk.api.durf_api import DURFApi
from inda_desk.api.generic_parsing_api import GenericParsingApi
from inda_desk.api.italian_identity_card_api import ItalianIdentityCardApi
from inda_desk.api.utilities_api import UtilitiesApi
from inda_desk.api.visura_api import VISURAApi
