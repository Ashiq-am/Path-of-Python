# Import Module
from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Image
login_btn = PhotoImage(file = "Image Path")

# Create button and image
img = Button(root, image = login_btn,
			borderwidth = 0)

img.pack()

# Execute Tkinter
root.mainloop()
