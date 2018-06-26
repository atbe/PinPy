from collections import Iterator

class PinterestPaginatedModel(Iterator):
    '''
    Iterator class to support paginated data from Pinterest
    '''

    def __init__(
            self,
            json_data,
            id,
            paginate_api_function=None,
            page_getter_func=None,
            page_setter_func=None,
            data_type=None):
        '''
        :param json_data: The json that represents this object as returned by the Pinterest API.
        :param id: The id of the board the pins belong to.
        :param paginate_api_function: API function call that retrieves next page of data.
        :param page_getter_func: Function called to get the next page
        :param page_setter_func: Function called to set the current page
        '''

        self._data = json_data
        self._items = list(json_data['data'])
        del json_data['data']
        self._id: str = id
        self._current: int = 0
        self._high: int = len(self._items)
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
        return self._data

    @property
    def status(self):
        return self._data['status']

    def update_contents(self, new_json):
        self._high += len(new_json['data'])
        self._items.extend(list(new_json['data']))
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
                return self._data_type(self._items[self._current - 1])
            return self._items[self._current - 1]


class BookmarkPagination(PinterestPaginatedModel):

    def __init__(self, json_data, id, api_paginate_function):
        def set_page(json, new_value):
            json['bookmark'] = new_value

        super().__init__(
            json_data,
            id,
            api_paginate_function,
            page_getter_func=lambda json: json.get('bookmark', None),
            page_setter_func=set_page)
