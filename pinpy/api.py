import json
import requests
import urllib.request
import pinpy

class API(object):
    """Pinterest API"""

    TIMEOUT = 20

    def __init__(self, access_token=None, v3_access_token=None,
                 host='https://api.pinterest.com', api_root='/v1',
                 wait_on_rate_limit=False, wait_on_rate_limit_notify=False):
        """ Api instance Constructor

        :param auth_handler:
        :param host:  url of the server of the rest api, default:'api.twitter.com'
        :param api_root: suffix of the api version, default:'/1.1'
        :param wait_on_rate_limit: If the api wait when it hits the rate limit, default:False
        :param wait_on_rate_limit_notify: If the api print a notification when the rate limit is hit, default:False
        """
        self.access_token = access_token
        self.v3_access_token = v3_access_token
        self.api_root = api_root
        self.host = host
        self.wait_on_rate_limit = wait_on_rate_limit
        self.wait_on_rate_limit_notify = wait_on_rate_limit_notify


    @staticmethod
    def call(url, method='get', params=None):
        """
        API call to Pinterest
            url: String, API endpoint with access token attached
            method:  String, HTTP method, get post put delete
            params: Dict, optional, supply necessary parameters
            fields: String, optional, expected return fields,
                will return default fields if not specified
        """
        result = getattr(requests, method)(url, timeout=API.TIMEOUT, data=params)
        # print (request.json())
        if result.status_code in [200, 201]:
            return result.json()
        elif result.status_code == 404:
            raise pinpy.exceptions.PinPyContentNotFoundError(response=result)
        else:
            raise pinpy.exceptions.PinPyUnhandledResponseCodeError(response=result)

    def get_me(self):
        """Get the authenticated user's Pinterest account info"""
        api_endpoint = self.host + self.api_root +'/me/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_likes(self):
        """Get the pins that the authenticated user likes"""
        api_endpoint = self.host + self.api_root +'/me/likes/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_followers(self):
        """Get the authenticated user's followers"""
        api_endpoint = self.host + self.api_root +'/me/followers/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_following_boards(self):
        """Get the boards that the authenticated user follows"""
        api_endpoint = self.host + self.api_root +'/me/following/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_following_users(self):
        """Get the Pinterest users that the authenticated user follows"""
        api_endpoint = self.host + self.api_root +'/me/following/users/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_following_interests(self):
        """Get the interests that the authenticated user follows"""
        api_endpoint = self.host + self.api_root +'/me/following/interests/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def follow_user(self, user_name):
        """Follow a user
		parameters:
             name: 'user_name',
             description: 'user name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/users/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', { 'user': user_name })


    def unfollow_user(self, user_name):
        """Unfollow a user
		parameters:
             name: 'user_name',
             description: 'user name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/users/' + user_name
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'delete')

    def follow_board(self, board_id):
        """Follow a board
		parameters:
             name: 'board_id',
             description: 'board name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', { 'board': board_id })

    def unfollow_board(self, board_id):
        """Unfollow a board
		parameters:
             name: 'board_id',
             description: 'board name'
		"""
        api_endpoint = self.host + self.api_root +'/me/following/boards/' + board_id
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'delete')

    def get_my_pins(self):
        """Get all of authenticated users's pins"""
        api_endpoint = self.host + self.api_root +'/me/pins/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url)

    def get_boards(self):
        """Get all of authenticated users's boards"""
        api_endpoint = self.host + self.api_root +'/me/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'get')

    def get_user(self, user_id):
        """GET - Gets data on a user using the /api_version/users/<user>/ endpoint

        Parameters
        ----------
        user_id : string
            The id of the user to retrieve.

        Returns
        -------
        json_array
            The response from Pinterest.

        Raises
        -------
        RuntimeError
            If the response code != 200, this exception will be raised along
            with the return code of the request.

        """
        api_endpoint = self.host + self.api_root + "/users/{:s}".format(user_id)
        request_url = api_endpoint + '?access_token=' + self.access_token
        desired_attributes = ['id', 'username', 'first_name', 'last_name', 'bio', 'created_at', 'counts', 'image']
        desired_attributes = [atr + '%2C' for atr in desired_attributes]
        request_url += "&fields={}".format(''.join(desired_attributes))
        request_url = request_url.rstrip('%2C')
        # print(request_url)
        return pinpy.User(API.call(request_url)['data'])

    def create_board(self, board_info):
        """Create a new board
        parameters:
             name: 'board name',
             description: 'Board description, optional'
        """
        api_endpoint = self.host + self.api_root +'/boards/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', board_info)

    def create_pin(self, pin_info):
        """Create a pin on a board
        pinInfo structure:
             board: '<username>/<board_name>' OR '<board_id>',
             note: 'My note'
             link: 'https://www.google.com',
             image_url: 'http://marketingland.com/pinterest-logo-white-1920.png'
        """
        api_endpoint = self.host + self.api_root +'/pins/'
        request_url = api_endpoint + '?access_token=' + self.access_token
        return API.call(request_url, 'post', pin_info)

    def get_public_pin(self, pin_id):
        """GET - Gets data on a pin using the /v1/pins/<pin>/ endpoint

        Parameters
        ----------
        pin_id : string
            The id of the pin to retrieve.

        Returns
        -------
        json_array
            The response from Pinterest.

        Raises
        -------
        RuntimeError
            If the response code != 200, this exception will be raised along
            with the return code of the request.

        """
        api_endpoint = self.host + self.api_root + "/pins/{:s}".format(pin_id)
        request_url = api_endpoint + '?access_token=' + self.access_token
        desired_attributes = ['attribution', 'board', 'color', 'counts', 'created_at', 'creator',
                              'id', 'image', 'link', 'media', 'metadata', 'note', 'original_link', 'url']
        desired_attributes = [atr + '%2C' for atr in desired_attributes]
        request_url += "&fields={}".format(''.join(desired_attributes))
        request_url = request_url.rstrip('%2C')
        # print(request_url)
        return pinpy.Pin(API.call(request_url)['data'])

    def get_public_board(self, board_id):
        """ Reference: https://developers.pinterest.com/docs/api/boards/

        GET - Gets all pins on a board using the /v1/boards/<board_spec:board>/pins/ endpoint

        Parameters
        ----------
        board_id : string
            The id of the board to retrieve.

        Returns
        -------
        json_array
            The response from Pinterest.

        Raises
        -------
        RuntimeError
            If the response code != 200, this exception will be raised along
            with the return code of the request.

        """
        api_endpoint = self.host + self.api_root + "/boards/{:s}".format(board_id)
        request_url = api_endpoint + '?access_token=' + self.access_token
        desired_attributes = ['counts', 'created_at', 'creator', 'description', 'id', 'image', 'name', 'url']
        desired_attributes = [atr + '%2C' for atr in desired_attributes]
        request_url += "&fields={}".format(''.join(desired_attributes))
        request_url = request_url.rstrip('%2C')
        # print(request_url)

        # build the user object, makes one call to API
        json_data = API.call(request_url)['data']
        json_data['creator'] = self.get_user(json_data['creator']['id'])

        return pinpy.Board(json_data)

    def get_public_board_pins(self, board_id, cursor=None):
        """ Reference: https://developers.pinterest.com/docs/api/boards/

        GET - Gets all pins on a board using the /v1/boards/<board_spec:board>/pins/ endpoint

        Parameters
        ----------
        board_id : string
            The id of the board to retrieve.

        Returns
        -------
        json_array
            The response from Pinterest.

        Raises
        -------
        RuntimeError
            If the response code != 200, this exception will be raised along
            with the return code of the request.

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
        # print(request_url)
        if cursor:
            return API.call(request_url)
        else:
            return pinpy.BoardPins(API.call(request_url), board_id, self)

    def get_public_board_pins_v3(self, board_id, bookmark=None, page_size=100):
        '''
        EXPERIMENTAL

        Uses the API v3 endpoint to get the pins on a board. More flexible than v1 because of higher request
        limits and the ability to return up to 250 pins per request.

        :param board_id:
        :param bookmark: Bookmark of the request for pagination.
        :return:
        '''
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_public_board_pins_v3).')

        api_endpoint = "{}/{}/boards/{}/pins/".format(self.host, 'v3', board_id)
        # print(api_endpoint)
        if bookmark:
            request_url = "{}?page_size={}&bookmark={}&access_token={}".format(api_endpoint, page_size, bookmark, self.v3_access_token)
            return API.call(request_url)
        else:
            request_url = "{}?page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
            return pinpy.BoardPinsV3(API.call(request_url), board_id, self)


    def get_public_pin_v3(self, pin_id):
        """GET - Gets data on a pin using the /v3/pins/<pin>/ endpoint

        EXPERIMENTAL

        Uses the API v3 endpoint to get the pin. More flexible than v1 because of higher request limits and more data.

        Parameters
        ----------
        pin_id : string
            The id of the pin to retrieve.

        Returns
        -------
        json_array
            The response from Pinterest.

        Raises
        -------
        RuntimeError
            If the response code != 200, this exception will be raised along
            with the return code of the request.

        """
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_public_board_pins_v3).')

        api_endpoint = "{}/{}/pins/{}/".format(self.host, 'v3', pin_id)
        request_url = "{}?access_token={}".format(api_endpoint, self.v3_access_token)
        # print(request_url)
        return pinpy.PinV3(API.call(request_url)['data'])

    def get_user_v3(self, user_id):
        """GET - Gets data on a user using the /api_version/users/<user>/ endpoint

        Parameters
        ----------
        user_id : string
            The id of the user to retrieve.

        Returns
        -------
        json_array
            The response from Pinterest.

        Raises
        -------
        RuntimeError
            If the response code != 200, this exception will be raised along
            with the return code of the request.

        """
        api_endpoint = "{}/{}/users/{}/".format(self.host, 'v3', user_id)
        request_url = "{}?access_token={}".format(api_endpoint, self.v3_access_token)
        # print(request_url)
        # TODO: Make model
        return API.call(request_url)['data']

    def get_user_followers_v3(self, user_id, bookmark=None, page_size=100):
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_user_followers).')

        api_endpoint = "{}/{}/users/{}/followers/".format(self.host, 'v3', user_id)
        # print(api_endpoint)
        if bookmark:
            request_url = "{}?page_size={}&bookmark={}&access_token={}".format(api_endpoint, page_size, bookmark, self.v3_access_token)
            return API.call(request_url)
        else:
            request_url = "{}?page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
            return pinpy.UserFollowersV3(API.call(request_url), user_id, self.get_user_followers_v3)


    def get_user_following_v3(self, user_id, bookmark=None, page_size=100):
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_user_following_v3).')

        api_endpoint = "{}/{}/users/{}/following/".format(self.host, 'v3', user_id)
        # print(api_endpoint)
        if bookmark:
            request_url = "{}?page_size={}&bookmark={}&access_token={}".format(api_endpoint, page_size, bookmark, self.v3_access_token)
            return API.call(request_url)
        else:
            request_url = "{}?page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
            return pinpy.UserFollowingV3(API.call(request_url), user_id, self.get_user_following_v3)


    def get_board_v3(self, board_id):
        """GET - Gets data on a user using the /api_version/boards/<board_id>/ endpoint

        Parameters
        ----------
        board_id : string
            The id of the board to retrieve.

        Returns
        -------
        json_array
            The response from Pinterest.

        Raises
        -------
        PyPinContentNotFoundError
            If the response code == 404, this exception will be raised along
            with the return code of the request.
        PyPinUnhandledResponseCodeError
            For all other errors

        """
        api_endpoint = "{}/{}/boards/{}/".format(self.host, 'v3', board_id)
        request_url = "{}?access_token={}".format(api_endpoint, self.v3_access_token)
        # print(request_url)
        # TODO: Make model
        return API.call(request_url)['data']


    def get_user_pins_v3(self, user_id, bookmark=None, page_size=100):
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_user_pins_v3).')

        api_endpoint = "{}/{}/users/{}/pins/".format(self.host, 'v3', user_id)
        # print(api_endpoint)
        if bookmark:
            request_url = "{}?page_size={}&bookmark={}&access_token={}".format(api_endpoint, page_size, bookmark, self.v3_access_token)
            return API.call(request_url)
        else:
            request_url = "{}?page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
            return pinpy.UserPinsV3(API.call(request_url), user_id, self.get_user_pins_v3)

    def get_pin_comments_v3(self, pin_id, bookmark=None, page_size=100):
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_pin_comments_v3).')

        api_endpoint = "{}/{}/pins/{}/comments/".format(self.host, 'v3', pin_id)
        if bookmark:
            request_url = "{}?page_size={}&bookmark={}&access_token={}".format(api_endpoint, page_size, bookmark, self.v3_access_token)
            return API.call(request_url)
        else:
            request_url = "{}?page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
            return pinpy.PinCommentsV3(API.call(request_url), pin_id, self.get_pin_comments_v3)


    def get_visually_similar_pins(self, pin_id, bookmark=None, page_size=100):
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_similar_pins).')

        api_endpoint = f"{self.host}/v3/visual_search/flashlight/pin/{pin_id}/?x=0&y=0&w=1&h=1&"
        if bookmark:
            request_url = f"{api_endpoint}page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
            return API.call(request_url)
        else:
            request_url = "{}page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
            return pinpy.BookmarkPagination(API.call(request_url), pin_id, self.get_visually_similar_pins)

    def get_user_boards(self, user_id, bookmark=None, page_size=100):
        if not self.v3_access_token:
            raise RuntimeError('API v3 token not provided to API client! Cannot use this method (get_users_boards).')

        api_endpoint = f"{self.host}/v3/users/{user_id}/boards"
        if bookmark:
            request_url = f"{api_endpoint}/?page_size={page_size}&bookmark={bookmark}&access_token={self.v3_access_token}"
            return API.call(request_url)
        else:
            request_url = "{}/?page_size={}&access_token={}".format(api_endpoint, page_size, self.v3_access_token)
            return pinpy.BookmarkPagination(API.call(request_url), user_id, self.get_user_boards)
