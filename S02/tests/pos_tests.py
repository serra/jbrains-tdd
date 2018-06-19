from .context import pos
import unittest
from pos.terminal import Terminal


class TerminalTestCase(unittest.TestCase):
    def test_can_create_terminal(self):
        Terminal()

    def setUp(self):
        self.displayed_price = None

    def _price_callback(self, price):
        self.displayed_price = price

    def test_can_input_barcode(self):
        t = Terminal()
        t.add_item('a barcode', 'a price')
        t.on_barcode('a barcode')

    def test_displays_no_message_if_item_does_not_exist(self):
        t = Terminal()
        t.on_barcode('does not exist')
        self.assertIsNone(self.displayed_price)

    def test_can_display_a_price(self):
        t = Terminal(self._price_callback)
        t.add_item('12345', '25.00')
        t.on_barcode('12345')
        assert self.displayed_price == '25.00'

    def test_can_add_item_to_terminal(self):
        t = Terminal()
        t.add_item('12345', '25.00')

    def test_can_add_item_to_terminal_twice_last_price_counts(self):
        t = Terminal(self._price_callback)
        t.add_item('12345', '25.00')
        t.add_item('12345', '24.99')
        t.on_barcode('12345')
        assert self.displayed_price == '24.99'

    def test_can_add_item_and_return_price(self):
        t = Terminal(self._price_callback)
        t.add_item('210', '12.00')
        t.on_barcode('210')
        assert self.displayed_price == '12.00'