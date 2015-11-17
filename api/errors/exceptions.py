class BaseException(Exception):
    def __init__(self, resp):
        self.response = resp


class TwitterException(BaseException):
    def __str__(self):
        return "Twitter returned unexpected result\nResponse: {0}".format(
            self.response
        )


class WikipediaException(BaseException):
    def __str__(self):
        return "Wikipedia returned unexpected result\nResponse: {0}".format(
            self.response
        )


class NoBearerToken(Exception):
    def __str__(self):
        return "No Bearer Token"
