from .context import pos
import unittest
from pos.terminal import Terminal


class SellOneItemTestCase(unittest.TestCase):
    def test_can_create_terminal(self):
        Terminal(self.screen.display_price, dict())

    def setUp(self):
        self.catalog = {'12345': '25.00', '210': '12.00'}
        self.screen = ScreenMock()
        self.t = Terminal(self.screen.display_price, self.catalog)

    def test_can_input_barcode(self):
        self.t.on_barcode('12345')

    def test_show_friendly_message_if_item_does_not_exist(self):
        self.t.on_barcode('does not exist')
        assert self.screen.get_display_text(
        ) == 'unknown product: "does not exist"'

    def test_can_display_a_price(self):
        self.t.on_barcode('12345')
        assert self.screen.get_display_text() == '25.00'

    def test_can_display_price_of_another_item(self):
        self.t.on_barcode('210')
        assert self.screen.get_display_text() == '12.00'


class ScreenMock:
    def __init__(self):
        self.displayed_price = None

    # function to be able to verify the text in tests:
    def get_display_text(self):
        return self.displayed_price

    def display_price(self, price):
        self.displayed_price = price
