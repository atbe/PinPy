class PinPyException(Exception):
    def __init__(self, response=None):
        self.response = response


class PinPyContentNotFoundError(PinPyException):

    def __str__(self):
        return '404 response from Pinterest. Content not found.'

    def __repr__(self):
        return self.__str__()


class PinPyRateLimitMetException(PinPyException):

    def __str__(self):
        return '429 response from Pinterest. Rate limit met.'

    def __repr__(self):
        return self.__str__()


class PinPyUnhandledResponseCodeError(PinPyException):

    def __init__(self, response=None):
        super().__init__(response)

    def __str__(self):
        return 'Unhandled response code returned from Pinterest = {}'.format(self.response.status_code)

    def __repr__(self):
        return "{}:\nStatus Code={}".format(self.__str__str(), self.response.status_code)
