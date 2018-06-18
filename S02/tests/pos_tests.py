from .context import pos
import unittest
from pos.terminal import Terminal


class TerminalTestCase(unittest.TestCase):
    def test_can_create_terminal(self):
        Terminal()

    def test_can_input_barcode(self):
        t = Terminal()
        t.on_barcode('a barcode')

    @unittest.skip("this does not proof anything yet")
    def test_displays_no_message_if_item_does_not_exist(self):
        t = Terminal()
        t.on_barcode('does not exist')

    def test_can_display_a_price(self):
        self.displayed_price = None

        def _price_callback(price):
            self.displayed_price = price

        t = Terminal(_price_callback)
        t.on_barcode('12345')
        assert self.displayed_price == '25.00'

    def test_can_add_item_to_terminal(self):
        t = Terminal()
        t.add_item('12345', '25.00')
