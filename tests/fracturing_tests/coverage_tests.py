from .context import fracturing
import unittest
from fracturing.fraction_covering import function_to_lower_code_coverage, another_function_to_lower_coverage


class SubtractFractionsTestCase(unittest.TestCase):
    def test_can_subtract_fractions(self):
        function_to_lower_code_coverage()
        another_function_to_lower_coverage()
