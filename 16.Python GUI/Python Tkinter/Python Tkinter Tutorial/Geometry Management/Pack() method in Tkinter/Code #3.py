# Importing tkinter module
from tkinter import *
# from tkinter.ttk import *

# creating Tk window
master = Tk()

# cretaing a Fra, e which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)

# button widgets which can also expand and fill
# in the parent widget entirely
b1 = Button(pane, text = "Click me !",
			background = "red", fg = "white")
b1.pack(side = LEFT, expand = True, fill = BOTH)

b2 = Button(pane, text = "Click me too",
			background = "blue", fg = "white")
b2.pack(side = LEFT, expand = True, fill = BOTH)

b3 = Button(pane, text = "I'm also button",
			background = "green", fg = "white")
b3.pack(side = LEFT, expand = True, fill = BOTH)

mainloop()
