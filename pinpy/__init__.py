__version__ = '0.1'
__author__ = 'Ibrahim Ahmed'
__license__ = 'MIT'

from pinpy.api import API
from pinpy.models import Pin
from pinpy.models import Board
from pinpy.models import User
from pinpy.models import BoardPins
from pinpy.models import BoardPinsV3
from pinpy.models import UserFollowersV3
from pinpy.models import UserFollowingV3
from pinpy.models import UserPinsV3
from pinpy.models import PinV3
from pinpy.models import PinCommentsV3
from pinpy.models import BookmarkPagination
import pinpy.exceptions as exceptions

# Global, unauthenticated instance of API
api = API()