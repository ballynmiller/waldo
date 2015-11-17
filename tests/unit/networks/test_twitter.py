import unittest
import mock

from api.errors import exceptions
from api.networks import twitter


class TwitterNetworkTest(unittest.TestCase):

    def test_connection(self):
        connection = twitter.Twitter()
        self.assertIsInstance(connection, twitter.Twitter)

    @mock.patch('api.networks.twitter.requests')
    def test_search(self, mockedRequests):
        response = mock.Mock()
        response.json.return_value = {
            'access_token': 'TestToken',
            'statuses': [
                {
                    'created_at': "0",
                    'text': 'Testing'
                }
            ]
        }
        response.status_code = 200

        mockedRequests.post.return_value = response
        mockedRequests.get.return_value = response

        connection = twitter.Twitter()
        connection.request_token()

        self.assertEqual(connection.get_feed("test").create_response(), [
            {
                'application': 'twitter',
                'created_date': '0',
                'message': 'Testing'
            }
        ])

    def test_search_no_token(self):
        connection = twitter.Twitter()
        with self.assertRaises(exceptions.NoBearerToken):
            connection.get_feed("test")

    @mock.patch('api.networks.twitter.requests')
    def test_search_not_found(self, mockedRequests):
        response = mock.Mock()
        response.status_code = 500

        mockedRequests.get.return_value = response

        connection = twitter.Twitter()
        connection.bearer_token = True
        with self.assertRaises(exceptions.TwitterException):
            connection.get_feed("test")

    def test_token_request_found(self):
        connection = twitter.Twitter()
        connection.bearer_token = True

        self.assertIsNone(connection.request_token())

    @mock.patch('api.networks.twitter.requests')
    def test_invalidate_token_failure(self, mockedRequests):
        response = mock.Mock()
        response.status_code = 500

        mockedRequests.post.return_value = response

        with self.assertRaises(exceptions.TwitterException):
            connection = twitter.Twitter()
            connection.bearer_token = True
            connection.invalidate_token()

    @mock.patch('api.networks.twitter.requests')
    def test_invalidate_token(self, mockedRequests):
        response = mock.Mock()
        response.status_code = 200

        mockedRequests.post.return_value = response

        connection = twitter.Twitter()
        connection.bearer_token = True
        connection.invalidate_token()

        self.assertIsNone(connection.bearer_token)

    def test_invalidate_without_token(self):
        connection = twitter.Twitter()
        self.assertIsNone(connection.invalidate_token())

    # @mock.patch('api.networks.twitter.requests')
    # def test_search_failure(self):
    #
    #
    # @mock.patch('api.networks.twitter.requests')
    # def test_geo_search(self, mockedRequests):
    #     connection = twitter.Twitter()
    #     self.assertEqual(connection.get_feed("test", lat=0, lng=0), {
    #         "latitude": 0,
    #         "longitude": 0,
    #         "name": "test"
    #     })

    @mock.patch('api.networks.twitter.requests')
    def test_network_failure(self, mockedRequests):
        response = mock.Mock()
        response.status_code = 500
        mockedRequests.post.return_value = response

        connection = twitter.Twitter()
        with self.assertRaises(exceptions.TwitterException):
            connection.request_token()
