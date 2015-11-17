import unittest

from api.responses import base


class TestBaseResponse(unittest.TestCase):
    def test_format_not_implemented(self):
        class Test(base.BaseResponse):
            pass

        with self.assertRaises(NotImplementedError):
            test = Test([])
            test.format_response()

    def test_create_not_implemented(self):
        class Test(base.BaseResponse):
            pass

        with self.assertRaises(NotImplementedError):
            test = Test([])
            test.create_response()
