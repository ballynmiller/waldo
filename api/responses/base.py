class BaseResponse(object):
    def __init__(self, data):
        self.data = data

    def format_response(self):
        raise NotImplementedError

    def create_response(self):
        raise NotImplementedError
