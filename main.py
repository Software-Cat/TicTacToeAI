import tkinter as tk


root = tk.Tk()
root.title("Tic Tac Toe")

button1 = tk.Button(root, text=" ", height=4, width=8)
button1.grid(row=3, column=0)

button2 = tk.Button(root,  text=" ", height=4, width=8)
button2.grid(row=3, column=1)

button3 = tk.Button(root,  text=" ", height=4, width=8)
button3.grid(row=3, column=2)

button4 = tk.Button(root,  text=" ", height=4, width=8)
button4.grid(row=4, column=0)

button5 = tk.Button(root,  text=" ", height=4, width=8)
button5.grid(row=4, column=1)

button6 = tk.Button(root,  text=" ", height=4, width=8)
button6.grid(row=4, column=2)

button7 = tk.Button(root,  text=" ", height=4, width=8)
button7.grid(row=5, column=0)

button8 = tk.Button(root,  text=" ", height=4, width=8)
button8.grid(row=5, column=1)

button9 = tk.Button(root,  text=" ", height=4, width=8)
button9.grid(row=5, column=2)

tk.mainloop()
