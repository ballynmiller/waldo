import mock
import unittest

from api.errors import exceptions
from api.networks import wikipedia


class WikipediaNetworkTest(unittest.TestCase):

    def test_connection(self):
        connection = wikipedia.Wikipedia()
        self.assertIsInstance(connection, wikipedia.Wikipedia)

    @mock.patch('api.networks.wikipedia.requests')
    def test_search(self, mockedRequests):
        response = mock.Mock()
        response.json.return_value = {
            "query": {
                'search': [
                    {
                        "timestamp": "0",
                        "title": "Testing",
                        "snippet": "This is a test"
                    }
                ]
            }
        }
        response.status_code = 200

        mockedRequests.get.return_value = response
        connection = wikipedia.Wikipedia()
        self.assertEqual(connection.get_feed("test").create_response(), [
            {
                'application': 'wikipedia',
                'message': 'This is a test',
                'title': 'Testing',
                'created_date': '0'
            }
        ])

    # @mock.patch('api.networks.wikipedia.requests')
    # def test_geo_search(self, mockedRequests):
    #     connection = wikipedia.Wikipedia()
    #     self.assertEqual(connection.get_feed("test", lat=0, lng=0), {
    #         "latitude": 0,
    #         "longitude": 0,
    #         "name": "test"
    #     })

    @mock.patch('api.networks.wikipedia.requests')
    def test_network_failure(self, mockedRequests):
        connection = wikipedia.Wikipedia()

        response = mock.Mock()
        response.status_code = 500

        mockedRequests.get.return_value = response

        with self.assertRaises(exceptions.WikipediaException):
            connection.get_feed("test")
