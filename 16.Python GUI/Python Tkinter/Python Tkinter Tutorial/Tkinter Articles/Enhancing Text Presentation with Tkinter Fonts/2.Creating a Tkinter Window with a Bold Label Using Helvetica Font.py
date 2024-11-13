import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
font = tkFont.Font(family="Helvetica", size=12, weight="bold")
label = tk.Label(root, text="Hello, Tkinter!", font=font)
label.pack()
root.mainloop()
