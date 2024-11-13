# Python program to create color chooser dialog box

# importing tkinter module
from tkinter import *

# importing the color choose package
from tkinter import colorchooser


# Function that will be invoked when the
# button will be clicked in the main window
def color_choose():

	# variable to store hexadecimal code of color
	color_code = colorchooser.askcolor(title ="color choose")
	print(color_code)

root = Tk()
button = Button(root, text = "Select color",command = "color_choose")
button.pack()
root.geometry("300x300")
root.mainloop()
