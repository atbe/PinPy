class PyPinException(Exception):
    def __init__(self, response=None):
        self.response = response

class PyPinContentNotFoundError(PyPinException):

    def __str__(self):
        return '404 response from Pinterest. Content not found.'

    def __repr__(self):
        return self.__str__()

class PyPinUnhandledResponseCodeError(PyPinException):

    def __init__(self, response=None):
        super().__init__(response)

    def __str__(self):
        return 'Unhandled response code returned from Pinterest = {}'.format(self.response.status_code)

    def __repr__(self):
        return "{}:\nStatus Code={}".format(self.__str__str(), self.response.status_code)
