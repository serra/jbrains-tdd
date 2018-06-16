from .context import fracturing
import unittest
from fracturing.fraction import Fraction


class SubtractFractionsTestCase(unittest.TestCase):
    def test_can_subtract_fractions(self):
        assert Fraction(2, 3) - Fraction(1, 3) is not None

    def test_subtract_whole_numbers_gt_zero(self):
        assert Fraction(5) - Fraction(3) == Fraction(2)
