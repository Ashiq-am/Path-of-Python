# Import Module
from tkinter import *

# Create Object
root = Tk()

# specify size of window.
root.geometry("400x500")

# delete content from Text Box


def delete_text():
	T.delete("1.0", "end")


# Create text widget
T = Text(root)
T.pack()

# Create Delete Button
Button(root, text="Delete", command=delete_text).pack()

# Excute Tkinter
root.mainloop()
