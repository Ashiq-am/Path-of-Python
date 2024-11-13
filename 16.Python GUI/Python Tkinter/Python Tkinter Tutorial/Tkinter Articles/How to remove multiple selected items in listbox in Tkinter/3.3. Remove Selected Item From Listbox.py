# Import Module
from tkinter import *

# Function will remove selected Listbox items
def remove_item():
	selected_checkboxs = listbox.curselection()

	for selected_checkbox in selected_checkboxs[::-1]:
		listbox.delete(selected_checkbox)

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

Button(root, text="delete", command=remove_item).pack()

# Execute Tkinter
root.mainloop()
