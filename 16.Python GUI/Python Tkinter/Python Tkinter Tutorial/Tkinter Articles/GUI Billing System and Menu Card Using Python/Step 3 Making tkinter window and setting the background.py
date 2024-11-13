# import tkinter module
from tkinter import *

# make a window
window = Tk()

# specify it's size
window.geometry("700x600")

# take a image for background
bg = PhotoImage(file='bg.png')

# label it in the background
label17 = Label(window, image=bg)

# position the image as well
label17.place(x=0, y=0)

# closing the main loop
window.mainloop()
