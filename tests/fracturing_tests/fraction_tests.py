from .context import fracturing
import unittest
from fracturing.fraction import Fraction, ZeroDenominatorError


class FractionTestCase(unittest.TestCase):
    def test_can_create_fraction(self):
        f = Fraction(1, 2)
        assert f is not None

    def test_can_print_fraction(self):
        # this is useful in test output
        f = Fraction(1, 2)
        assert str(f) == '1/2'

    def test_can_not_create_fraction_with_zero_denominator(self):
        with self.assertRaises(ZeroDenominatorError):
            Fraction(1, 0)


class FractionRepresentationTestCase(unittest.TestCase):
    def test_fractions_are_in_lowest_terms(self):
        assert Fraction(2, 3) == Fraction(2, 3)
        assert Fraction(4, 6) == Fraction(2, 3)
        assert Fraction(5, 4) == Fraction(5, 4)
        assert Fraction(15, 12) == Fraction(5, 4)

    def test_fractions_are_improper_and_not_mixed(self):
        assert str(Fraction(37, 17)) != '2 3/17'
        assert Fraction(37, 17) == Fraction(37, 17)


class FractionEqualityTestCase(unittest.TestCase):
    def test_equality_of_fractions(self):
        assert Fraction(2, 3) == Fraction(2, 3)

    def test_inequality_of_fractions(self):
        assert Fraction(2, 3) != Fraction(4, 7)

    def test_fractions_as_if_reduced(self):
        assert Fraction(2, 3) == Fraction(4, 6)

    def test_initial_location_of_sign_does_not_matter_for_equality(self):
        assert Fraction(-1, 2) == Fraction(1, -2)

    def test_double_negative_equals_positive(self):
        assert Fraction(-1, -2) == Fraction(1, 2)