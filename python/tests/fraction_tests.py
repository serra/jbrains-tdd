from .context import fraction
import unittest
from fraction.arithmetic import Fraction


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

    def test_to_lowest_terms(self):
        print(str(Fraction(2, 3)))
        assert str(Fraction(2, 3)) == '2/3'
        print(str(Fraction(4, 6)))
        assert str(Fraction(4, 6)) == '2/3'

    # express fractions as lowest terms (4/6 becomes 2/3)

    # express fractions as improper and not mixed (7/5 does NOT become 1 2/7)

    # add

    # need to be able treat fractions as normal numbers
    # e.g.: can do 4 + 9 wit fractions as with numbers

    # subtract

    # multiply

    # divide

    # 0 denominator not allowed
