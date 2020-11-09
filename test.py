import unittest
import main


class TestEnvironment(unittest.TestCase):

    def test_tk_version(self):
        self.assertGreaterEqual(main.tk.TkVersion, 8.6)
