import unittest
import mock

from api.networks import base


class NetworkBaseTest(unittest.TestCase):
    def test_not_implemented(self):
        class Testing(base.NetworkBase):
            pass

        connection = Testing()
        with self.assertRaises(NotImplementedError):
            connection.get_feed("test")
