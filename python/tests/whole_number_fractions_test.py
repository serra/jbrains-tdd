from .context import fracturing
import unittest
from fracturing.fraction import Fraction


class WholeNumberFractionsTestCase(unittest.TestCase):
    def test_one_as_fraction(self):
        assert Fraction(1) == Fraction(1, 1)

    def test_some_other_whole_number(self):
        assert Fraction(5) == Fraction(5, 1)
        assert Fraction(3) == Fraction(3, 1)

    def test_negative_whole_number(self):
        assert Fraction(-3) == Fraction(-3, 1)

    def test_zero_whole_number(self):
        assert Fraction(0) == Fraction(0, 1)
        assert Fraction(0) == Fraction(0, 5)

    def test_addition(self):
        assert Fraction(1) + Fraction(0) == Fraction(1)
        assert Fraction(0) + Fraction(0) == Fraction(0)
        assert Fraction(2) + Fraction(5) == Fraction(7)
