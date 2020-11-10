import tkinter as tk
import enum
import random
from tkinter import Grid


class Game(tk.Frame):
    @enum.unique
    class GridState(enum.Enum):
        EMPTY = ""
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

        self.turn = random.choice([self.GridState.X, self.GridState.O])

    def create_widgets(self):
        self.matrix = []

        for row in range(3):
            currentRow = []
            for column in range(3):
                button = tk.Button()
                button.config(
                    width=3, height=1,
                    text=self.GridState.EMPTY,
                    command=lambda context=button: self.button_press_callback(
                        context),
                    font=("JetBrains Mono", 36, "bold")
                )
                button.grid(row=row, column=column)
                currentRow.append(button)
            self.matrix.append(currentRow)

    def button_press_callback(self, context: tk.Button):
        print("Button Pressed")
        if self.GridState(context["text"]) == self.GridState.EMPTY:
            context["text"] = self.turn
            context["state"] = tk.DISABLED
            self.switch_players()

    def switch_players(self):
        if self.turn is self.GridState.O:
            self.turn = self.GridState.X
        else:
            self.turn = self.GridState.O


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Tic Tac Toe')
    root.resizable(False, False)

    game = Game(root)

    root.mainloop()
