from .context import pos
import unittest
from pos.terminal import Terminal


class SellOneItemTestCase(unittest.TestCase):
    def test_can_create_terminal(self):
        Terminal(self.displayed_price, dict())

    def setUp(self):
        self.catalog = {'12345': '25.00', '210': '12.00'}
        self.t = Terminal(self._price_callback, self.catalog)
        self.displayed_price = None

    def _price_callback(self, price):
        self.displayed_price = price

    def test_can_input_barcode(self):
        self.t.on_barcode('12345')

    def test_displays_no_message_if_item_does_not_exist(self):
        self.t.on_barcode('does not exist')
        self.assertIsNone(self.displayed_price)

    def test_can_display_a_price(self):
        self.t.on_barcode('12345')
        assert self.displayed_price == '25.00'

    def test_can_display_price_of_another_item(self):
        self.t.on_barcode('210')
        assert self.displayed_price == '12.00'