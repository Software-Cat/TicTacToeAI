import unittest
import tkinter as tk
import _tkinter
import main


class TKinterTestCase(unittest.TestCase):
    """Common methods used for every GUI test.
    """

    def setUp(self):
        self.root = tk.Tk()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass


class TestButtons(TKinterTestCase):
    def test_button_num(self):
        game = main.Game(self.root)

        self.pump_events()

        self.assertEqual(len(game.grid), 3)
        self.assertEqual(len(game.grid[0]), 3)
        self.assertEqual(len(game.grid[1]), 3)
        self.assertEqual(len(game.grid[2]), 3)

    def test_button_press(self):
        pass
