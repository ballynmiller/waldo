import unittest

from mock import patch


class TestApplication(unittest.TestCase):

    @patch('requests')
    def test_feeds(self, mockedRequests):
        self.assertEqual(connection.get_feeds(), [
            {
                "application": "twitter",
                "message": "message"
            },
            {
                "application": "Wikipedia",
                "message": "message"
            }
        ]

    @patch('requests')
    def test_geo_feeds(self, mockedRequests):
        self.assertEqual(connection.get_feeds("test", lat=0, lng=0), [
            {
                "application": "twitter",
                "message": "message",
                "latitude": 0,
                "longitude": 0
            },
            {
                "application": "Wikipedia",
                "message": "message",
                "latitude": 0,
                "longitude": 0
            }
        ])

    @patch('requests')
    def test_single_failure(self, mockedRequests):
        self.assertEqual(connection.get_feeds("test"), [
            {
                "application": "twitter",
                "message": "message",
                "latitude": 0,
                "longitude": 0
            }
        ])

    @patch('requests')
    def test_complete_failure(self, mockedRequests):
        self.assertEqual(connection.get_feeds(), 500)
