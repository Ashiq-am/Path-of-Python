# importing required packages
import tkinter
from PIL import ImageTk, Image
import os

# creating main window
root = tkinter.Tk()

# loading the image
img = ImageTk.PhotoImage(Image.open("gfg.jpeg"))

# reading the image
panel = tkinter.Label(root, image = img)

# setting the application
panel.pack(side = "bottom", fill = "both",expand = "yes")

# running the application
root.mainloop()
