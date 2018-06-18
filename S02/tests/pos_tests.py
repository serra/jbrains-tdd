from .context import pos
import unittest
from pos.terminal import hello


class FractionTestCase(unittest.TestCase):
    def test_can_say_hello(self):
        hello()
