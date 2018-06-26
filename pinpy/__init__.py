__version__ = '0.1'
__author__ = 'Ibrahim Ahmed'
__license__ = 'MIT'

from pinpy.api import API
from pinpy.models import BookmarkPagination
import pinpy.exceptions as exceptions

# Global, unauthenticated instance of API
api = API()