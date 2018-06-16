from .context import fracturing
import unittest
from .fraction_tests import _f


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
