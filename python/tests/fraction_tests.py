from .context import fraction
import unittest


class OkCounterTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three_ok(self):
        assert 3 == 2
