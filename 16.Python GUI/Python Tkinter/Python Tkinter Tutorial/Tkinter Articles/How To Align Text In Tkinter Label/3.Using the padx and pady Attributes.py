# import tkinter module
from tkinter import Tk, Label

# create main window
root = Tk()

# Adding horizontal padding to center the text
label_padx = Label(root, text="Centered Text with Padding", padx=20)
label_padx.pack(pady=10, padx=10, anchor="w")

root.mainloop()
