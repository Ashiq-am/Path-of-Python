# Importing all functions/classes
# from tkinter module
from tkinter import *

# toplevel window
root = Tk()

# widget whose grid info is to be obtained
rect = Label(root,
			text = "MY GRID INFO IS SHOWN BELOW",
			bg = "pink")

# grid method is used for placing
# the widgets at respective positions
# in table like structure .
rect.grid(stick = N)

# create a label
label = Label(root)

label.grid()

label['text'] = rect.grid_info()

# start the GUI
root.mainloop()
