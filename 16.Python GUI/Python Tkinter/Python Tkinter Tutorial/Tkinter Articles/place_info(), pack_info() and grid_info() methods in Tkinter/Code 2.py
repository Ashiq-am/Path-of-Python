# Importing all functions/classes
# from tkinter module
from tkinter import *

# toplevel window
root = Tk()

# create a Label widget whose
# pack info is to be obtained
rect = Label(root,
			text = "MY PACK INFO IS SHOWN BELOW",
			bg = "pink")

# placing them in a specific position
# in the parent widget.
rect.pack(expand = True)

# create a Label
label = Label(root)

label.pack()

label['text'] = rect.pack_info()

# start the GUI
root.mainloop()
