import mock
import unittest

from api.exceptions import exceptions


class ExceptionTests(unittest.TestCase):
    def test_twitter_exception(self):
        response = mock.Mock()
        exception = exceptions.TwitterException(response)

        self.assertEqual(
            (
                "Twitter returned unexpected result\n" +
                "Response: {0}".format(response)
            ), str(exception)
        )

    def test_wikipedia_exception(self):
        response = mock.Mock()
        exception = exceptions.WikipediaException(response)

        self.assertEqual(
            (
                "Wikipedia returned unexpected result\n" +
                "Response: {0}".format(response)
            ), str(exception)
        )

    def test_bearer_exception(self):
        exception = exceptions.NoBearerToken()

        self.assertEqual(
            (
                "No Bearer Token"
            ), str(exception)
        )
