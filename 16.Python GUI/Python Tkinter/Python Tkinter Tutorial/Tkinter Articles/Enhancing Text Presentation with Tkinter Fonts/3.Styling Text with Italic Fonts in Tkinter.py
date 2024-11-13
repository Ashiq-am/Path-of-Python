import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
font = tkFont.Font(family="Arial", size=10, slant="italic", underline=1)
label = tk.Label(root, text="Styled Text", font=font)
label.pack()
root.mainloop()
