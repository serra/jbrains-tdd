from .context import fraction
import unittest
from fraction.arithmetic import Fraction
from fraction.arithmetic import add


class FractionTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_create_fraction(self):
        f = Fraction(1, 2)
        assert f is not None

    def test_can_print_fraction(self):
        f = Fraction(1, 2)
        assert str(f) == '1/2'

    def test_fractions_are_in_lowest_terms(self):
        assert str(Fraction(2, 3)) == '2/3'
        assert str(Fraction(4, 6)) == '2/3'
        assert str(Fraction(5, 4)) == '5/4'
        assert str(Fraction(15, 12)) == '5/4'

    def test_fractions_are_improper_and_not_mixed(self):
        assert str(Fraction(37, 17)) != '2 3/17'
        assert str(Fraction(37, 17)) == '37/17'

    def test_add_fractions(self):
        assert str(add(Fraction(1, 3), Fraction(1, 2))) == '5/6'

    # add

    # need to be able treat fractions as normal numbers
    # e.g.: can do 4 + 9 wit fractions as with numbers

    # subtract

    # multiply

    # divide

    # 0 denominator not allowed
