from .context import fracturing
import unittest
from fracturing.fraction import Fraction


class SubtractFractionsTestCase(unittest.TestCase):
    def test_can_subtract_fractions(self):
        assert Fraction(2, 3) - Fraction(1, 3) is not None
