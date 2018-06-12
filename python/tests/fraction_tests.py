from .context import fracturing
import unittest
from fracturing.fraction import Fraction


def _f(a, b):
    return Fraction(a, b)


class FractionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_create_fraction(self):
        f = _f(1, 2)
        assert f is not None

    def test_can_print_fraction(self):
        f = _f(1, 2)
        assert str(f) == '1/2'

    def test_fractions_are_in_lowest_terms(self):
        assert str(_f(2, 3)) == '2/3'
        assert str(_f(4, 6)) == '2/3'
        assert str(_f(5, 4)) == '5/4'
        assert str(_f(15, 12)) == '5/4'

    def test_fractions_are_improper_and_not_mixed(self):
        assert str(_f(37, 17)) != '2 3/17'
        assert _f(37, 17) == _f(37, 17)

    def test_add_fractions(self):
        assert _f(1, 3) + _f(1, 2) == _f(5, 6)
        assert _f(1, 6) + _f(1, 3) == _f(1, 2)

    def test_add_like_normal_numbers(self):
        assert _f(1, 3) + _f(1, 2) == _f(5, 6)

    def test_equality_of_fractions(self):
        assert _f(2, 3) == _f(2, 3)
        assert _f(2, 3) == _f(4, 6)
        assert _f(2, 3) != _f(4, 7)
