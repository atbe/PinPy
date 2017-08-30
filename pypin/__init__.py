__version__ = '0.1'
__author__ = 'Ibrahim Ahmed'
__license__ = 'MIT'

from pypin.api import API
from pypin.models import Pin
from pypin.models import Board
from pypin.models import User
from pypin.models import BoardPins
from pypin.models import BoardPinsV3
from pypin.models import UserFollowersV3
from pypin.models import UserFollowingV3
from pypin.models import UserPinsV3
from pypin.models import PinV3
from pypin.models import PinCommentsV3
import pypin.exceptions as exceptions

# Global, unauthenticated instance of API
api = API()