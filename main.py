import tkinter as tk
import enum
import random
import aibase
from typing import List


AI_MODULE_NAME = "randomai"


class Game(tk.Frame):
    @enum.unique
    class State(enum.Enum):
        NULL = ""
        O = "O"
        X = "X"

        def __init__(self, state: str) -> None:
            self.state = state

        def __str__(self) -> str:
            return self.state

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0)
        self.create_widgets()

        self.turn = random.choice([self.State.X, self.State.O])
        self.message["text"] = str(self.turn) + "'s turn!"

        self.ai: aibase.AIBase
        self.ai = __import__(AI_MODULE_NAME).AI()

    def create_widgets(self):
        self.matrix: List[List[tk.Button]]
        self.matrix = []

        for row in range(3):
            currentRow = []
            for column in range(3):
                button = tk.Button(self.master)
                button.config(
                    width=3, height=1,
                    text=self.State.NULL,
                    command=lambda context=button: self.button_press_callback(
                        context),
                    font=("JetBrains Mono", 36, "bold")
                )
                button.grid(row=row, column=column)
                currentRow.append(button)
            self.matrix.append(currentRow)

        self.message = tk.Label(self.master, font=(
            "JetBrains Mono", 12, "normal"))
        self.message.grid(row=3, column=0, columnspan=3)

    def button_press_callback(self, context: tk.Button):
        context["text"] = self.turn
        context["state"] = tk.DISABLED

        if self.detect_win() != self.State.NULL:
            self.disable_all()
            self.message["text"] = str(self.detect_win()) + " is the winner!"
        else:
            if self.turn is self.State.X:
                self.message["text"] = "O's turn!"
            else:
                self.message["text"] = "X's turn!"

        self.switch_players()

    def switch_players(self):
        if self.turn is self.State.O:
            self.turn = self.State.X
        else:
            self.turn = self.State.O

    def disable_all(self):
        for row in self.matrix:
            for button in row:
                button["state"] = tk.DISABLED

    def detect_win(self) -> State:
        for column in range(3):
            if self.matrix[column][0]["text"] == self.matrix[column][1]["text"] == self.matrix[column][2]["text"]:
                return self.State(self.matrix[column][0]["text"])

        for row in range(3):
            if self.matrix[0][row]["text"] == self.matrix[1][row]["text"] == self.matrix[2][row]["text"]:
                return self.State(self.matrix[0][row]["text"])

        if self.matrix[0][0]["text"] == self.matrix[1][1]["text"] == self.matrix[2][2]["text"]:
            return self.State(self.matrix[0][0]["text"])

        if self.matrix[2][0]["text"] == self.matrix[1][1]["text"] == self.matrix[0][2]["text"]:
            return self.State(self.matrix[2][0]["text"])

        return self.State.NULL

    def ai_ticking(self):
        if self.turn is self.State.X:
            # Update AI matrix
            grid = []
            for row in range(3):
                currentRow = []
                for column in range(3):
                    currentRow.append(self.State(
                        self.matrix[column][row]["text"]))
                grid.append(currentRow)
            self.ai.matrix = grid

            # Process AI turn
            action = self.ai.__turn__()
            if action:
                self.matrix[action[1]][action[0]].invoke()

        # Recursion
        self.master.after(1000, self.ai_ticking)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Tic Tac Toe')
    root.resizable(False, False)

    game = Game(root)
    game.ai_ticking()

    root.mainloop()
