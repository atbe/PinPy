import requests
import pinpy
import logging
import time

log = logging.getLogger('pinpy.api')


class API(object):
	"""Pinterest API"""

	TIMEOUT = 20

	def __init__(
			self,
			access_token=None,
			v3_access_token=None,
			host='https://api.pinterest.com',
			api_root='/v1',
			wait_on_rate_limit=False,
			wait_on_rate_limit_notify=False):
		"""
		Api instance Constructor


		:param access_token: API Access Token (v1)
		:param v3_access_token: API Access Token (v3)
		:param host: API host url (defaults to https://api.pinterest.com)
		:param api_root: suffix of the api version, default:'/1', (alternative is /v1) (only used internally)
		:param wait_on_rate_limit: If the api wait when it hits the rate limit, default:False
		:param wait_on_rate_limit_notify: If the api print a notification when the rate limit is hit, default:False
		"""
		self.access_token = access_token
		self.v3_access_token = v3_access_token
		self.api_root = api_root
		self.host = host
		self.wait_on_rate_limit = wait_on_rate_limit
		self.wait_on_rate_limit_notify = wait_on_rate_limit_notify

	def call(self, url, method='get', params=None):
		"""
		API call to Pinterest

		:param url: String, API endpoint with access token attached
		:param method:  String, HTTP method, defaults to get (get post put delete)
		:param params: Dict, optional, supply necessary parameters
		"""
		sleep_time = 60
		while True:
			result = getattr(requests, method)(url, timeout=API.TIMEOUT, data=params)

			if result.status_code in [200, 201]:
				return result.json()

			elif result.status_code == 404:
				raise pinpy.exceptions.PinPyContentNotFoundError(response=result)

			elif result.status_code == 429:
				if not self.wait_on_rate_limit:
					raise pinpy.exceptions.PinPyRateLimitMetException(response=result)

				if self.wait_on_rate_limit_notify:
					log.warning("Rate limit reached. Sleeping for: %d" % sleep_time)
				time.sleep(sleep_time)
				sleep_time *= 2
			else:
				raise pinpy.exceptions.PinPyUnhandledResponseCodeError(response=result, endpoint=url)

	def get_me(self):
		"""
		Get the authenticated user's Pinterest account info

		:rtype: Dict of user profile data.
		"""

		request_url = f"{self.host}{self.api_root}/me/?access_token={self.access_token}"
		return self.call(request_url)

	def get_likes(self):
		"""
		Get the pins that the authenticated users likes

		:rtype: List of authenticated users likes
		"""

		request_url = f"{self.host}{self.api_root}/me/likes/?access_token={self.access_token}"
		return self.call(request_url)

	def get_followers(self):
		"""
		Get the authenticated user's followers

		:rtype: List of followers
		"""

		request_url = f"{self.host}{self.api_root}/me/followers/?access_token={self.access_token}"
		return self.call(request_url)

	def get_following_boards(self):
		"""
		Get the boards that the authenticated user follows

		:rtype: List of boards
		"""

		request_url = f"{self.host}{self.api_root}/me/following/boards/?access_token={self.access_token}"
		return self.call(request_url)

	def get_following_users(self):
		"""
		Get the Pinterest users that the authenticated user follows

		:rtype: List of users
		"""

		request_url = f"{self.host}{self.api_root}/me/following/users/?access_token={self.access_token}"
		return self.call(request_url)

	def get_following_interests(self):
		"""
		Get the interests that the authenticated user follows

		:rtype: List of interests
		"""

		request_url = f"{self.host}{self.api_root}/me/following/interests/?access_token={self.access_token}"
		return self.call(request_url)

	def follow_user(self, user_name):
		"""
		Follow a user

		:param user_name: Username of user to follow
		"""

		request_url = f"{self.host}{self.api_root}/me/following/users/?access_token={self.access_token}"
		return self.call(request_url, 'post', {'user': user_name})

	def unfollow_user(self, user_name):
		"""
		Unfollow a user

		:param user_name: Username of user to unfollow
		"""

		request_url = f"{self.host}{self.api_root}/me/following/users/{user_name}?access_token={self.access_token}"
		return self.call(request_url, 'delete')

	def follow_board(self, board_id):
		"""
		Follow a board

		:param board_id: ID of board to follow
		"""

		request_url = f"{self.host}{self.api_root}/me/following/boards/?access_token={self.access_token}"
		return self.call(request_url, 'post', {'board': board_id})

	def unfollow_board(self, board_id):
		"""
		Unfollow a board

		:param board_id: ID of board to unfollow
		"""

		request_url = f"{self.host}{self.api_root}/me/following/boards/{board_id}?access_token={self.access_token}"
		return self.call(request_url, 'delete')

	def get_my_pins(self):
		"""
		Get all of authenticated users's pins

		:rtype: List of pins
		"""

		request_url = f"{self.host}{self.api_root}/me/pins/?access_token={self.access_token}"
		return self.call(request_url)

	def get_boards(self):
		"""
		Get all of authenticated users's boards

		:rtype: List of boards
		"""

		request_url = f"{self.host}{self.api_root}/me/boards?access_token={self.access_token}"
		return self.call(request_url, 'get')

	def get_user(self, user_id):
		"""
		Gets specific users profile

		:param user_id: ID of user whose profile will be collected
		:rtype: Dict of user data
		"""

		request_url = f"{self.host}{self.api_root}/users/{str(user_id)}?access_token={self.access_token}"
		desired_attributes = ['id', 'username', 'first_name', 'last_name', 'bio', 'created_at', 'counts', 'image']
		desired_attributes = [atr + '%2C' for atr in desired_attributes]
		request_url += f"&fields={''.join(desired_attributes)}"
		request_url = request_url.rstrip('%2C')
		return self.call(request_url)['data']

	def create_board(self, board_info):
		"""
		Create a new board

		:param board_info: Board info
		"""

		request_url = f"{self.host}{self.api_root}/boards/?access_token={self.access_token}"
		return self.call(request_url, 'post', board_info)

	def create_pin(self, pin_info):
		"""
		Create a pin on a board

		pin_info structure:
			board: '<username>/<board_name>' OR '<board_id>',
			note: 'My note'
			link: 'https://www.google.com',
			image_url: 'http://marketingland.com/pinterest-logo-white-1920.png'

		:param pin_info: Pin info
		"""

		request_url = f"{self.host}{self.api_root}/pins/?access_token={self.access_token}"
		return self.call(request_url, 'post', pin_info)

	def get_public_pin(self, pin_id):
		"""
		Gets a single pin

		:param pin_id: ID of pin to collect
		:rtype: Dict of pin data
		"""

		request_url = f"{self.host}{self.api_root}/pins/{pin_id}?access_token={self.access_token}"
		desired_attributes = ['attribution', 'board', 'color', 'counts', 'created_at', 'creator',
							  'id', 'image', 'link', 'media', 'metadata', 'note', 'original_link', 'url']
		desired_attributes = [atr + '%2C' for atr in desired_attributes]
		request_url += "&fields={}".format(''.join(desired_attributes))
		request_url = request_url.rstrip('%2C')
		return self.call(request_url)['data']

	def get_public_board(self, board_id):
		"""
		Gets public board data

		:param board_id: ID of board to collect
		"""

		request_url = f"{self.host}{self.api_root}/boards/{board_id}?access_token={self.access_token}"
		desired_attributes = ['counts', 'created_at', 'creator', 'description', 'id', 'image', 'name', 'url']
		desired_attributes = [atr + '%2C' for atr in desired_attributes]
		request_url += "&fields={}".format(''.join(desired_attributes))
		request_url = request_url.rstrip('%2C')

		return self.call(request_url)['data']

	def get_public_board_pins(self, board_id, cursor=None):
		"""
		Gets all pins on a board (paginated)

		:param board_id: ID of board to collect
		:param cursor: Cursor used for pagination
		:rtype: List of pins (paginated)
		"""

		desired_attributes = ['attribution', 'board', 'color', 'counts', 'created_at', 'creator',
		                      'id', 'image', 'link', 'media', 'metadata', 'note', 'original_link', 'url']
		desired_attributes = [atr + '%2C' for atr in desired_attributes]
		api_endpoint = self.host + self.api_root + "/boards/{:s}/pins".format(str(board_id))
		if cursor:
			request_url = "{}?cursor={}&access_token={}".format(api_endpoint, cursor, self.access_token)
		else:
			request_url = "{}?access_token={}".format(api_endpoint, self.access_token)
		request_url += "&fields={}".format(''.join(desired_attributes))
		request_url = request_url.rstrip('%2C')
		if cursor:
			return self.call(request_url)
		else:
			return pinpy.BookmarkPagination(self.call(request_url), board_id, self.get_public_board_pins)

	def get_public_board_pins_v3(self, board_id, bookmark=None, page_size=100):
		"""
		Collects the pins in a board

		:param board_id: ID of board whos pins will be collected
		:param bookmark: Pinterest API bookmark used for pagination
		:param page_size: Number of items to collect for pagination
		:rtype: List of pins found in the board (paginated)
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Can\'t this method (get_public_board_pins_v3).')

		api_endpoint = f"{self.host}/v3/boards/{board_id}/pins/"
		if bookmark:
			request_url = f"{api_endpoint}?page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
			return self.call(request_url)
		else:
			request_url = f"{api_endpoint}?page_size={page_size}&access_token={self.v3_access_token}"
			return pinpy.BookmarkPagination(self.call(request_url), board_id, self.get_public_board_pins_v3)

	def get_public_pin_v3(self, pin_id):
		"""
		Collect a single Pin

		:param pin_id: Pin ID of PIN to collect
		:rtype: Dict of pin data
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_public_board_pins_v3).')

		api_endpoint = f"{self.host}/v3/pins/{pin_id}/"
		request_url = f"{api_endpoint}?access_token={self.v3_access_token}"
		return self.call(request_url)['data']

	def get_user_v3(self, user_id):
		"""
		Collect a particular users profile

		:param user_id: User ID to collect
		:rtype: Dict of user data
		"""

		api_endpoint = "{}/{}/users/{}/".format(self.host, 'v3', user_id)
		request_url = "{}?access_token={}".format(api_endpoint, self.v3_access_token)
		return self.call(request_url)['data']

	def get_user_followers_v3(self, user_id, bookmark=None, page_size=100):
		"""
		Collect a users followers

		:param user_id: User ID whose followers will be collected
		:param bookmark: Pinterest API bookmark used for pagination
		:param page_size: Number of items to collect for pagination
		:rtype: List of user profiles (paginated)
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_user_followers).')

		api_endpoint = f"{self.host}/v3/users/{user_id}/followers/"
		if bookmark:
			request_url = f"{api_endpoint}?page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
			return self.call(request_url)
		else:
			request_url = f"{api_endpoint}?page_size={page_size}&access_token={self.v3_access_token}"
			return pinpy.BookmarkPagination(self.call(request_url), user_id, self.get_user_followers_v3)

	def get_user_following_v3(self, user_id, bookmark=None, page_size=100):
		"""
		Collect the users someone follows

		:param user_id: User ID of user whose followees will be collected
		:param bookmark: Pinterest API bookmark used for pagination
		:param page_size: Number of items to collect for pagination
		:rtype: List of user profiles (the followees)
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_user_following_v3).')

		api_endpoint = f"{self.host}/v3/users/{user_id}/following/"
		if bookmark:
			request_url = f"{api_endpoint}?page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
			return self.call(request_url)
		else:
			request_url = f"{api_endpoint}?page_size={page_size}&access_token={self.v3_access_token}"
			return pinpy.BookmarkPagination(self.call(request_url), user_id, self.get_user_following_v3)

	def get_board_v3(self, board_id):
		"""
		Collect a board from Pinterest

		:param board_id: Board ID of board to collect
		:rtype: Dict containing board data
		"""

		api_endpoint = f"{self.host}/v3/boards/{board_id}/"
		request_url = f"{api_endpoint}?access_token={self.v3_access_token}"
		# print(request_url)
		return self.call(request_url)['data']

	def get_user_pins_v3(self, user_id, bookmark=None, page_size=100):
		"""
		Collect a users pins

		:param user_id: User ID of user whose pins will be collected
		:param bookmark: Pinterest API bookmark used for pagination
		:param page_size: Number of items to collect for pagination
		:rtype: List of pins (paginated)
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_user_pins_v3).')

		api_endpoint = f"{self.host}/v3/users/{user_id}/pins/"
		if bookmark:
			request_url = f"{api_endpoint}?page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
			return self.call(request_url)
		else:
			request_url = f"{api_endpoint}?page_size={page_size}&access_token={self.v3_access_token}"
			return pinpy.BookmarkPagination(self.call(request_url), user_id, self.get_user_pins_v3)

	def get_pin_comments_v3(self, pin_id, bookmark=None, page_size=100):
		"""
		Collect the comments made on a Pin

		:param pin_id: Pin ID to collect the comments from
		:param bookmark: Pinterest API bookmark used for pagination
		:param page_size: Number of items to collect for pagination
		:rtype: List of comments (paginated)
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_pin_comments_v3).')

		api_endpoint = f"{self.host}/v3/pins/{pin_id}/comments/"
		if bookmark:
			request_url = f"{api_endpoint}?page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
			return self.call(request_url)
		else:
			request_url = f"{api_endpoint}?page_size={page_size}&access_token={self.v3_access_token}"
			return pinpy.BookmarkPagination(self.call(request_url), pin_id, self.get_pin_comments_v3)

	def get_visually_similar_pins(self, pin_id, bookmark=None, page_size=100):
		"""
		Collect visually similar Pins of a particular Pin.
		NOTICE: This endpoint is rate limited

		:param pin_id: Pin ID to collect the similar pins of
		:param bookmark: Pinterest API bookmark used for pagination
		:param page_size: Number of items to collect for pagination
		:rtype: List of similar pins (paginated)
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_similar_pins).')

		api_endpoint = f"{self.host}/v3/visual_search/flashlight/pin/{pin_id}/?x=0&y=0&w=1&h=1&"
		if bookmark:
			request_url = f"{api_endpoint}page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
			return self.call(request_url)
		else:
			request_url = "{}page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
			return pinpy.BookmarkPagination(self.call(request_url), pin_id, self.get_visually_similar_pins)

	def get_user_boards(self, user_id, bookmark=None, page_size=100):
		"""
		Collect a users boards

		:param user_id: ID of user whose boards will be collected
		:param bookmark: Pinterest API bookmark used for pagination
		:param page_size: Number of items to collect for pagination
		:rtype: List of users boards (paginated)
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_users_boards).')

		api_endpoint = f"{self.host}/v3/users/{user_id}/boards"
		if bookmark:
			request_url = f"{api_endpoint}/?page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
			return self.call(request_url)
		else:
			request_url = "{}/?page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
			return pinpy.BookmarkPagination(self.call(request_url), user_id, self.get_user_boards)

	def get_pin(self, pin_id):
		"""
		Collect a single pin

		:param pin_id: ID of pin to collect
		:rtype: Dict containing pin data
		"""

		if not self.v3_access_token:
			raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_users_boards).')

		api_endpoint = f"{self.host}/v3/pins/{pin_id}"
		request_url = f"{api_endpoint}/?access_token={self.v3_access_token}"
		return self.call(request_url)['data']
