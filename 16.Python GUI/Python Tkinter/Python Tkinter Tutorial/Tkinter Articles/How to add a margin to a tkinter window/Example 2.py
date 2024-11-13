# importing the module
from tkinter import *

# container window
root = Tk()

# frame
frame = Frame(root)

# content of the frame
frame.text = Text(root)
frame.text.insert('1.0', 'Geeks for Geeks')

# to add margin to the frame
frame.text.grid(row = 0, column = 1,
				padx = 20, pady = 20)

# simple button
frame.quitw = Button(root)
frame.quitw["text"] = "Logout",
frame.quitw["command"] = root.quit
frame.quitw.grid(row = 1, column = 1)

root.mainloop()
