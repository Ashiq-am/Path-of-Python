# Import Module
from tkinter import *

# Create Object
root = Tk()
# set Geometry
root.geometry('400x200')


# Add Labels and Buttons
Label(root, text = "IMAGE CONVERSION",
	font = "italic 15 bold").pack(pady = 10)

Button(root, text = "Select Images", font = 14).pack(pady = 10)

frame = Frame()
frame.pack(pady = 20)

Button(frame, text = "Image to PDF", relief = "solid",
				bg = "white", font = 15).pack(side = LEFT,padx = 10)

Button(frame, text = "Images to PDF", relief = "solid",
				bg = "white",font = 15).pack()

# Execute Tkinter
root.mainloop()
