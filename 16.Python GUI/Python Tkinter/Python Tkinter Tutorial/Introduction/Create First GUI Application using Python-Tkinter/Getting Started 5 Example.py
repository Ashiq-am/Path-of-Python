from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# function to display text when
# button is clicked
def clicked():
	lbl.configure(text = "I just got clicked")

# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,fg = "red", command=clicked)

btn.grid(column=1, row=0)

root.mainloop()
