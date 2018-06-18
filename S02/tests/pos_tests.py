from .context import pos
import unittest
from pos.terminal import Terminal


class TerminalTestCase(unittest.TestCase):
    def test_can_create_terminal(self):
        Terminal()

    def test_can_input_barcode(self):
        t = Terminal()
        t.on_barcode('a barcode')
