# Importing tkinter module
from tkinter import *

# Creating a tkinter window
root = Tk()

# Initialize tkinter window with dimensions 300 x 250
root.geometry('300x250')

# Creating a Button
btn = Button(root, text = 'Click me !', command = root.destroy)

# Set a relative position of button
btn.pack(side=RIGHT, padx=15, pady=20)

root.mainloop()
