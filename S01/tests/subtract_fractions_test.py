from .context import fracturing
import unittest
from fracturing.fraction import Fraction


class SubtractFractionsTestCase(unittest.TestCase):
    def test_can_subtract_fractions(self):
        assert Fraction(2, 3) - Fraction(1, 3) is not None

    def test_subtract_whole_numbers_positive_result(self):
        assert Fraction(5) - Fraction(3) == Fraction(2)

    def test_subtract_whole_numbers_negative_result(self):
        assert Fraction(3) - Fraction(5) == Fraction(-2)

    def test_can_subtract_fractions_with_same_denominator(self):
        assert Fraction(2, 3) - Fraction(1, 3) == Fraction(1, 3)
        assert Fraction(1, 5) - Fraction(3, 5) == Fraction(-2, 5)

    def test_substract_will_return_fraction_in_lowest_terms(self):
        assert str(Fraction(7, 15) - Fraction(4, 15)) == '1/5'
        assert str(Fraction(4, 15) - Fraction(7, 15)) == '-1/5'

    def test_subtract_with_different_denominators(self):
        assert Fraction(3, 7) - Fraction(1, 4) == Fraction(5, 28)
        assert Fraction(2, 3) - Fraction(1, 5) == Fraction(7, 15)
