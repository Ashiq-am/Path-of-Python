# Import Module
from tkinter import *

# Create Object
root = Tk()

# Set Geometry
root.geometry("200x200")

# Add Listbox
listbox = Listbox(root, selectmode=MULTIPLE)
listbox.pack()

# Listbox Items List
items = ["Apple", "Orange", "Grapes", "Banana", "Mango"]

# Iterate Through Items list
for item in items:
	listbox.insert(END, item)

Button(root, text="delete").pack()

# Execute Tkinter
root.mainloop()
