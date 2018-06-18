from .context import pos
import unittest
from pos.terminal import Terminal


class TerminalTestCase(unittest.TestCase):
    def test_can_create_terminal(self):
        Terminal()
