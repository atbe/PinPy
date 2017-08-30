from collections import Iterator
from datetime import datetime

class JsonDataWrapper:
    '''
    Reference: http://stackoverflow.com/questions/38464302/wrapping-a-python-class-around-json-data-which-is-better

    '''

    def __init__(self, json_data):
        '''
        Interface between API reference and underlying implementation through json.

        :param json_data: The json representation of the object as provided by the API.
        '''
        self._data = json_data

    def get(self, name):
        '''

        :param name: Key to search for in self.json_data
        :return: Value corresponding to key 'name' in self.json_data
        '''
        return self._data[name]


class Pin(JsonDataWrapper):
    '''
    API Reference: https://developers.pinterest.com/docs/api/pins/?
    '''

    def __init__(self, json_data):
        # TODO: Confirm timezone of Pin._created_at.
        # TODO: Create class container for Pin._attribution. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.

        :param _id: The unique string of numbers and letters that identifies the Pin on Pinterest.
        :param _link: Hyperlink to the pin.
        :param _url: The URL of the Pin on Pinterest.
        :param _creator: Pinterest user that created the pin. models.PinterestUser
        :param _board: Pinterest board the Pin is on. models.Board
        :param _created_at: The date the Pin was created. ISO 8601.
        :param _note: The user-entered description of the Pin.
        :param _color: The dominant color of the Pin’s image in hex code format.
        :param _repin_count: Number of repins this Pin has. NOT constant.
        :param _comment_count: Number of comments this Pin has. NOT constant.
        :param _like_count: Number of likes this Pin has. NOT constant.
        :param _attribution: The source data for videos, including the title, URL, provider, author name, author URL and provider name.

        '''
        json_data['created_at'] = datetime.strptime(json_data['created_at'], '%Y-%m-%dT%H:%M:%S')
        super().__init__(json_data)

        self._id = None
        self._link = None
        self._url = None
        self._creator = None
        self._board = None
        self._created_at = None
        self._note = None
        self._color = None
        self._counts = None
        self._media = None
        self._attribution = None
        self._image = None
        self._metadata = None
        self._repin_count = None
        self._comment_count = None
        self._like_count = None

        self._original_link = None

    @property
    def id(self): return self.get('id')

    @property
    def link(self): return self.get('link')

    @property
    def url(self): return self.get('url')

    @property
    def creator(self): return self.get('creator')

    @property
    def board(self): return self.get('board')

    @property
    def created_at(self): return self.get('created_at')

    @property
    def original_link(self): return self.get('original_link')

    @property
    def note(self): return self.get('note')

    @property
    def color(self): return self.get('color')

    @property
    def link(self): return self.get('link')

    @property
    def board(self): return self.get('board')

    @property
    def image(self): return self.get('image')

    @property
    def repin_count(self): return self.get('counts').get('repins')

    @property
    def comment_count(self): return self.get('counts').get('comments')

    @property
    def like_count(self): return self.get('counts').get('likes')

    @property
    def metadata(self): return self.get('metadata')


class Board(JsonDataWrapper):
    '''
    API Reference: https://developers.pinterest.com/docs/api/boards/
    '''

    def __init__(self, json_data):
        # TODO: Confirm timezone of Board._created_at.
        # TODO: Create class container for Board._image. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.

        :param _id: The unique string of numbers and letters that identifies the board on Pinterest.
        :param _name: The name of the board.
        :param _url: The link to the board.
        :param _description: The user-entered description of the board.
        :param _creator: The creator of the board. pypin.models.User.
        :param _created_at: The date the board was created. ISO 8601 format.
        :param _pin_count: Number of pins on the board. NOT constant.
        :param _collaborator_count: Number of collaborators on the board. NOT constant.
        :param _follower_count: Number of followers this board has. NOT constant.
        :param _image: The board’s profile image. The response returns the image’s URL, width and height.

        '''
        super().__init__(json_data)

        self._counts = None
        self._created_at = None
        self._description = None
        self._id = None
        self._image = None
        self._name = None
        self._url = None
        self._creator = None

    @property
    def pin_count(self): return self.get('counts').get('pins')

    @property
    def collaborator_count(self): return self.get('counts').get('collaborators')

    @property
    def follower_count(self): return self.get('counts').get('followers')

    @property
    def created_at(self): return self.get('created_at')

    @property
    def description(self): return self.get('description')

    @property
    def id(self): return self.get('id')

    @property
    def image(self): return self.get('image')

    @property
    def name(self): return self.get('name')

    @property
    def url(self): return self.get('url')

    @property
    def creator(self): return self.get('creator')


class User(JsonDataWrapper):
    '''
    API Reference: https://developers.pinterest.com/docs/api/users/
    '''

    def __init__(self, json_data):
        # TODO: Confirm timezone of User._created_at.
        # TODO: Create class container for User._image. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.

        :param _id: The unique string of numbers and letters that identifies the user on Pinterest.
        :param _username: The user’s Pinterest username.
        :param _first_name: The user’s first name.
        :param _last_name: The user’s last name.
        :param _bio: The text in the user’s “About you” section in their profile.
        :param _created_at: The date the user created their account. ISO 8601 format.
        :param _pin_count: Number of pins the user has posted and are available. NOT constant.
        :param _follower_count: Number of followers this user has. NOT constant.
        :param _following_count: Number of accounts this user is following. NOT constant.
        :param _board_count: Number of boards this user has. NOT constant.
        :param _like_count: Number of likes this user has. NOT constant.
        :param _image: The user’s profile image. The response returns the image’s URL, width and height.
        '''
        super().__init__(json_data)

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._bio = None
        self._created_at = None
        self._pin_count = None
        self._follower_count = None
        self._board_count = None
        self._like_count = None
        self._image = None

    @property
    def id(self): return self.get('id')

    @property
    def username(self): return self.get('username')

    @property
    def first_name(self): return self.get('first_name')

    @property
    def last_name(self): return self.get('last_name')

    @property
    def bio(self): return self.get('bio')

    @property
    def created_at(self): return self.get('created_at')

    @property
    def pin_count(self): return self.get('counts').get('pins')

    @property
    def following_count(self): return self.get('counts').get('following')

    @property
    def follower_count(self): return self.get('counts').get('followers')

    @property
    def board_count(self): return self.get('counts').get('boards')

    @property
    def like_count(self): return self.get('counts').get('likes')

    @property
    def image(self): return self.get('image')



class BoardPins(JsonDataWrapper, Iterator):
    '''
    API Reference: https://developers.pinterest.com/docs/api/users/
    '''

    def __init__(self, json_data, board_id, api):
        # TODO: Confirm timezone of User._created_at.
        # TODO: Create class container for User._image. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.
        :param api: The api to be used while this BoardPins object exists.

        :param _id: The id of the board the pins belong to.
        :param _api: The api stored for this BoardPins object.
        '''

        # use a list instead
        json_data['data'] = list(json_data['data'])

        super().__init__(json_data)
        self._id = board_id
        self._api = api
        self._current = 0
        self._high = len(self.pins)

    @property
    def id(self): return self._id

    @property
    def cursor(self): return self.get('page').get('cursor')

    @property
    def pins(self): return self.get('data')

    def update_contents(self, new_json):
        self._high += len(new_json['data'])
        self.pins.extend(list(new_json['data']))
        self._data['page']['cursor'] = new_json['page']['cursor']

    def __next__(self):
        if self._current >= self._high:
            if self.cursor == None:
                # reset current so the user can iterate over the pins again
                self._current = 0
                raise StopIteration
            else:
                json_data = self._api.get_public_board_pins(self.id, self.cursor)
                self.update_contents(json_data)
                return self.__next__()
        else:
            self._current += 1
            return Pin(self.pins[self._current - 1])

class BoardPinsV3(JsonDataWrapper, Iterator):
    '''
    API Reference: https://developers.pinterest.com/docs/api/users/
    '''

    def __init__(self, json_data, board_id, api):
        # TODO: Confirm timezone of User._created_at.
        # TODO: Create class container for User._image. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.
        :param api: The api to be used while this BoardPins object exists.

        :param _id: The id of the board the pins belong to.
        :param _api: The api stored for this BoardPins object.
        '''

        # use a list instead
        # json_data['data'] = list(json_data['data'])

        super().__init__(json_data)
        self._id = board_id
        self._api = api
        self._current = 0
        self._high = len(self.pins)

    @property
    def id(self): return self._id

    @property
    def bookmark(self):
        if 'bookmark' not in self._data:
            return None
        return self.get('bookmark')

    @property
    def pins(self): return self.get('data')

    def update_contents(self, new_json):
        self._high += len(new_json['data'])
        self.pins.extend(list(new_json['data']))
        self._data['bookmark']= new_json.get('bookmark', None)

    def __next__(self):
        if self._current >= self._high:
            if self.bookmark == None:
                # reset current so the user can iterate over the pins again
                self._current = 0
                raise StopIteration
            else:
                json_data = self._api.get_public_board_pins_v3(self.id, self.bookmark)
                self.update_contents(json_data)
                return self.__next__()
        else:
            self._current += 1
            return self.pins[self._current - 1]

class PinV3(JsonDataWrapper):
    '''
    API Reference: https://developers.pinterest.com/docs/api/pins/?
    '''

    def __init__(self, json_data):
        # TODO: Confirm timezone of Pin._created_at.
        # TODO: Create class container for Pin._attribution. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.

        :param _id: The unique string of numbers and letters that identifies the Pin on Pinterest.
        :param _link: Hyperlink to the pin.
        :param _url: The URL of the Pin on Pinterest.
        :param _creator: Pinterest id of the user who made the pin.
        :param _board: Pinterest Board id this pin belongs to.
        :param _created_at: The date the Pin was created. ISO 8601.
        :param _note: The user-entered description of the Pin.
        :param _color: The dominant color of the Pin’s image in hex code format.
        :param _repin_count: Number of repins this Pin has. NOT constant.
        :param _comment_count: Number of comments this Pin has. NOT constant.
        :param _like_count: Number of likes this Pin has. NOT constant.
        :param _attribution: The source data for videos, including the title, URL, provider, author name, author URL and provider name.

        '''
        json_data['created_at'] = datetime.strptime(json_data['created_at'], '%a, %d %b %Y %H:%M:%S %z')
        super().__init__(json_data)

        self._id = None
        self._link = None
        self._creator = None
        self._board = None
        self._created_at = None
        self._note = None
        self._color = None
        self._attribution = None
        self._image = None
        self._metadata = None
        self._repin_count = None
        self._comment_count = None
        self._like_count = None

        self._original_link = None

    def to_json(self):
        return self._data

    @property
    def id(self): return self.get('id')

    @property
    def link(self): return self.get('shareable_url')

    @property
    def creator(self): return self.get('pinner').get('id')

    @property
    def board(self): return self.get('board').get('id')

    @property
    def created_at(self): return self.get('created_at')

    @property
    def note(self): return self.get('description')

    @property
    def color(self): return self.get('dominant_color')

    @property
    def repin_count(self): return self.get('repin_count')

    @property
    def comment_count(self): return self.get('comment_count')

    @property
    def like_count(self): return self.get('like_count')

    @property
    def attribution(self): return self.get('attribution')

    # TODO Find better represention.
    @property
    def image(self): return self.get('image_medium_url')

    @property
    def original_link(self): return self.get('link')


class PinterestPaginatedModel(JsonDataWrapper, Iterator):
    '''
    API Reference: https://developers.pinterest.com/docs/api/users/
    '''

    def __init__(self, json_data, id, paginate_api_function=None,
                 page_getter_func=None, page_setter_func=None, data_type=None):
        # TODO: Confirm timezone of User._created_at.
        # TODO: Create class container for User._image. Currently <dict>.
        '''

        :param json_data: The json that represents this object as returned by the Pinterest API.
        :param api: The api to be used while this BoardPins object exists.

        :param _id: The id of the board the pins belong to.
        :param _api: The api stored for this BoardPins object.
        '''

        # use a list instead
        json_data['data'] = list(json_data['data'])

        super().__init__(json_data)
        self._id = id
        self._current = 0
        self._high = len(self.items)
        self._paginate_api_function = paginate_api_function
        self._page_getter_func = page_getter_func
        self._page_setter_func = page_setter_func
        self._data_type = data_type

    @property
    def id(self):
        return self._id

    @property
    def cursor(self):
        return self._page_getter_func(self._data)

    @property
    def items(self):
        return self.get('data')

    def update_contents(self, new_json):
        self._high += len(new_json['data'])
        self.items.extend(list(new_json['data']))
        self._page_setter_func(self._data, self._page_getter_func(new_json))

    def __next__(self):
        if self._current >= self._high:
            if self.cursor == None:
                # reset current so the user can iterate over the pins again
                self._current = 0
                raise StopIteration
            else:
                json_data = self._paginate_api_function(self.id, self.cursor)
                self.update_contents(json_data)
                return self.__next__()
        else:
            self._current += 1
            if self._data_type is not None:
                return self._data_type(self.items[self._current - 1])
            return self.items[self._current - 1]


class UserFollowersV3(PinterestPaginatedModel):
    '''
    API Reference: https://developers.pinterest.com/docs/api/users/
    '''
    def __init__(self, json_data, user_id, api_paginate_function):
        def set_page(json, new_value):
            json['bookmark'] = new_value

        super().__init__(json_data, user_id, api_paginate_function,
                         page_getter_func=lambda json: json.get('bookmark', None),
                         page_setter_func=set_page)


class UserFollowingV3(PinterestPaginatedModel):

    def __init__(self, json_data, user_id, api_paginate_function):
        def set_page(json, new_value):
            json['bookmark'] = new_value

        super().__init__(json_data, user_id, api_paginate_function,
                         page_getter_func=lambda json: json.get('bookmark', None),
                         page_setter_func=set_page)


class UserPinsV3(PinterestPaginatedModel):

    def __init__(self, json_data, user_id, api_paginate_function):
        def set_page(json, new_value):
            json['bookmark'] = new_value

        super().__init__(json_data, user_id, api_paginate_function,
                         page_getter_func=lambda json: json.get('bookmark', None),
                         page_setter_func=set_page)


class PinCommentsV3(PinterestPaginatedModel):

    def __init__(self, json_data, pin_id, api_paginate_function):
        def set_page(json, new_value):
            json['bookmark'] = new_value

        super().__init__(json_data, pin_id, api_paginate_function,
                         page_getter_func=lambda json: json.get('bookmark', None),
                         page_setter_func=set_page)