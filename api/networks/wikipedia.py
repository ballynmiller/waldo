import base
import requests

from ..exceptions import exceptions


class Wikipedia(base.NetworkBase):
    def get_feed(self, query, lat=0, lng=0):
        payload = {
            'action': 'query',
            'list': 'search',
            'srsearch': str(query),
            'format': 'json'
        }

        resp = requests.get(
            url="https://en.wikipedia.org/w/api.php",
            params=payload
        )

        if resp.status_code is not 200:
            raise exceptions.WikipediaException(resp)

        return resp.json()['search']
