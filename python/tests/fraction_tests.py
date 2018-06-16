from .context import fracturing
import unittest
from fracturing.fraction import Fraction, ZeroDenominatorError


def _f(a, b):
    return Fraction(a, b)


class FractionTestCase(unittest.TestCase):
    def test_can_create_fraction(self):
        f = _f(1, 2)
        assert f is not None

    def test_can_print_fraction(self):
        # this is useful in test output
        f = _f(1, 2)
        assert str(f) == '1/2'

    def test_can_not_create_fraction_with_zero_denominator(self):
        with self.assertRaises(ZeroDenominatorError):
            Fraction(1, 0)


class FractionRepresentationTestCase(unittest.TestCase):
    def test_fractions_are_in_lowest_terms(self):
        assert _f(2, 3) == _f(2, 3)
        assert _f(4, 6) == _f(2, 3)
        assert _f(5, 4) == _f(5, 4)
        assert _f(15, 12) == _f(5, 4)

    def test_fractions_are_improper_and_not_mixed(self):
        assert str(_f(37, 17)) != '2 3/17'
        assert _f(37, 17) == _f(37, 17)


class AddFractionsTestCase(unittest.TestCase):
    def test_add_fractions(self):
        assert _f(1, 3) + _f(1, 2) == _f(5, 6)
        assert _f(1, 6) + _f(1, 3) == _f(1, 2)
        assert _f(1, 2) + _f(1, 2) == _f(1, 1)
        assert _f(1, 12) + _f(2, 12) == _f(1, 4)
        assert _f(7, 9) + _f(5, 9) == _f(4, 3)

    def test_add_with_zeros(self):
        assert _f(0, 2) + _f(0, 2) == _f(0, 2)
        assert _f(0, 13) + _f(1, 2) == _f(1, 2)

    def test_add_like_normal_numbers_use_plus_operator(self):
        assert _f(1, 3) + _f(1, 2) == _f(5, 6)


class FractionEqualityTestCase(unittest.TestCase):
    def test_equality_of_fractions(self):
        assert _f(2, 3) == _f(2, 3)
        assert _f(2, 3) == _f(4, 6)
        assert _f(2, 3) != _f(4, 7)
