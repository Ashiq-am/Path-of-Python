# import tkinter module
from tkinter import *

# Create Object
root = Tk()

# Initialize tkinter window with dimensions 100x100
root.geometry('300x300')

text=Text(root,
		width = 50,
		height = 50,
		padx = 10,
		pady = 10)

# pack the text-Aera in the window
text.pack()

root.mainloop()
