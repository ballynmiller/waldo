import unittest

from api import networks
from mock import patch


class WikipediaNetworkTest(unittest.TestCase):

    @patch('api.networks.Wikipedia.requests')
    def test_connection(self, mockedRequests):
        connection = networks.Wikipedia()
        self.assertTrue(connection.status())

    @patch('api.networks.Wikipedia.requests')
    def test_search(self, mockedRequests):
        connection = networks.Wikipedia()
        self.assertEqual(connection.get_feed("test"), {
            "name": "test"
        })

    @patch('api.networks.Wikipedia.requests')
    def test_geo_search(self, mockedRequests):
        connection = networks.Wikipedia()
        self.assertEqual(connection.get_feed("test", lat=0, lng=0), {
            "latitude": 0,
            "longitude": 0,
            "name": "test"
        })

    @patch('api.networks.Wikipedia.requests')
    def test_network_failure(self, mockedRequests):
        connection = networks.Wikipedia()
        self.assertRaises(connection.get_feed(), 504)
