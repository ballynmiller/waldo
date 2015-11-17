from api.responses import base


class TwitterResponse(base.BaseResponse):
    def format_response(self, data):
        model = {
            'application': 'twitter',
            'created_date': data['created_at'],
            'message': data['text'],
        }

        return model

    def create_response(self):
        return [self.format_response(data) for data in self.data]
