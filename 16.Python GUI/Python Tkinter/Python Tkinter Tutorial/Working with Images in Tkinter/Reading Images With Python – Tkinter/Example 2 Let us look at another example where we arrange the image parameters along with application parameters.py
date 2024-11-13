# importing required packages
import tkinter
from tkinter import NW

from PIL import ImageTk, Image

# creating main window
root = tkinter.Tk()

# arranging application parameters
canvas = tkinter.Canvas(root, width = 500,height = 250)

canvas.pack()

# loading the image
img = ImageTk.PhotoImage(Image.open("gfg.png"))

# arranging image parameters
# in the application
canvas.create_image(135, 20, anchor = NW, image = img)

# running the application
root.mainloop()
