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

    def __init__(self, response=None, endpoint=None):
        super().__init__(response)
        self.endpoint = endpoint

    def __str__(self):
        return f"Unhandled response code returned from Pinterest = {self.response.status_code} while hitting:\n{self.endpoint}"

    def __repr__(self):
        return "{}:\nStatus Code={}".format(self.__str__(), self.response.status_code)
