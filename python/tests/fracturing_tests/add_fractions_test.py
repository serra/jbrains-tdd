from .context import fracturing
import unittest
from fracturing.fraction import Fraction


class AddFractionsTestCase(unittest.TestCase):
    def test_add_fractions(self):
        assert Fraction(1, 3) + Fraction(1, 2) == Fraction(5, 6)
        assert Fraction(1, 6) + Fraction(1, 3) == Fraction(1, 2)
        assert Fraction(1, 2) + Fraction(1, 2) == Fraction(1, 1)
        assert Fraction(1, 12) + Fraction(2, 12) == Fraction(1, 4)
        assert Fraction(7, 9) + Fraction(5, 9) == Fraction(4, 3)

    def test_add_with_zeros(self):
        assert Fraction(0, 2) + Fraction(0, 2) == Fraction(0, 2)
        assert Fraction(0, 13) + Fraction(1, 2) == Fraction(1, 2)

    def test_add_like_normal_numbers_use_plus_operator(self):
        assert Fraction(1, 3) + Fraction(1, 2) == Fraction(5, 6)
