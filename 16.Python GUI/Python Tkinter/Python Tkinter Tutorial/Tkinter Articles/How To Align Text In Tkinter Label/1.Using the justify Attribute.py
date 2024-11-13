# import tkinter module
from tkinter import Tk, Label

# create main window
root = Tk()

# Left-aligned text
label_left = Label(root, text="Left Aligned Text", justify="left")
label_left.pack(pady=10, padx=10, anchor="w")

# Center-aligned text
label_center = Label(root, text="Center Aligned Text", justify="center")
label_center.pack(pady=10, padx=50, anchor="w")

# Right-aligned text
label_right = Label(root, text="Right Aligned Text", justify="right")
label_right.pack(pady=10, padx=100, anchor="w")

root.mainloop()
