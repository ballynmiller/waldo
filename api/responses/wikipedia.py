from api.responses import base


class WikipediaResponse(base.BaseResponse):
    def format_response(self, data):
        model = {
            'application': 'wikipedia',
            'created_date': data['timestamp'],
            'message': data['snippet'],
            'title': data['title']
        }

        return model

    def create_response(self):
        return [self.format_response(data) for data in self.data]
