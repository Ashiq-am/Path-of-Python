# Create a windoe
from tkinter import Tk
from tkinter.ttk import Button

root = Tk()

# Set Title as Image Loader
root.title("Image Loader")

# Set the resolution of window
root.geometry("550x300 + 300 + 150")

# Allow Window to be resizable
root.resizable(width = True, height = True)

# Create a button and place it into the window using grid layout
def open_img():
	pass


btn = Button(root, text ='open image', command = open_img).grid(row = 1, columnspan = 4)
root.mainloop()






'''The Button object is created with text ‘open image’. On clicking it the 
open_image function will be invoked.'''
