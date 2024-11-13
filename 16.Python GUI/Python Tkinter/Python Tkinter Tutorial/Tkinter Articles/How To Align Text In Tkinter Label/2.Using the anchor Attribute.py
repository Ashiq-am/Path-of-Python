# import tkinter module
from tkinter import Tk, Label

# create main window
root = Tk()

# Anchoring text to the west (left)
label_west = Label(root, text="Left Aligned Text", anchor="w")
label_west.pack(pady=10, padx=10, anchor="w")

# Anchoring text to the center
label_center = Label(root, text="Centre Aligned Text", anchor="center")
label_center.pack(pady=10, padx=50, anchor="w")

# Anchoring text to the east (right)
label_east = Label(root, text="Right Aligned Text", anchor="e")
label_east.pack(pady=10, padx=100, anchor="w")

root.mainloop()
