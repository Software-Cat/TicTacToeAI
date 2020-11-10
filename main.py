import tkinter as tk


class Game:
    def __init__(self, master=None):
        self.master = master
        self.grid = []

        for row in range(3):
            currentRow = []
            for column in range(3):
                btn = tk.Button(text="", width=12, height=6)
                btn.grid(row=row, column=column)
                currentRow.append(btn)
            self.grid.append(currentRow)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Tic Tac Toe')
    root.resizable(False, False)

    game = Game(root)

    root.mainloop()
