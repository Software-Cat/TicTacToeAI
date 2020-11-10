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


class TestLogic(TKinterTestCase):
    def test_turn_switch(self):
        game = main.Game(self.root)

        game.matrix[0][0].invoke()
        game.matrix[1][1].invoke()
        self.pump_events()

        self.assertNotEqual(
            game.matrix[0][0]["text"], game.matrix[1][1]["text"])

    def test_win_condition(self):
        game = main.Game(self.root)

        game.matrix[0][0].invoke()
        game.matrix[0][1].invoke()
        game.matrix[0][2].invoke()
        game.matrix[1][0].invoke()
        game.matrix[1][1].invoke()
        game.matrix[1][2].invoke()
        game.matrix[2][0].invoke()
        self.pump_events()

        self.assertNotEqual(game.detect_win(), game.GridState.NULL)


class TestButtons(TKinterTestCase):
    def test_button_num(self):
        game = main.Game(self.root)

        self.assertEqual(len(game.matrix), 3)
        self.assertEqual(len(game.matrix[0]), 3)
        self.assertEqual(len(game.matrix[1]), 3)
        self.assertEqual(len(game.matrix[2]), 3)

        for row in range(3):
            for column in range(3):
                self.assertIsInstance(game.matrix[column][row], tk.Button)

    def test_button_press(self):
        for row in range(3):
            for column in range(3):
                game = main.Game(self.root)
                currentTurn = game.turn

                game.matrix[column][row].invoke()
                self.pump_events()

                self.assertEqual(currentTurn, game.GridState(
                    game.matrix[column][row]["text"]))
