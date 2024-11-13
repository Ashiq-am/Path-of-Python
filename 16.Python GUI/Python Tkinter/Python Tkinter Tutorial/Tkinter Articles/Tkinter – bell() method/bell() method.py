# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Bell function
def bell():
	# call bell method
	root.bell()

# Add button
Button(root,text="Bell",command=bell).pack()

# Execute tkinter
root.mainloop()
