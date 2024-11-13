# Importing all functions/classes
# from tkinter module
from tkinter import *

# toplevel window
root = Tk()

# setting window size
root.geometry("810x350")

# create a Label widget whose
# place info is to be obtained
rect = Label(root,
			text = "MY PLACE INFO IS SHOWN BELOW",
			bg = "pink")

# place a widget in a specific
# position in the parent widget.
rect.place(rely = 0.1, relx = 0.2,
		relwidth = 0.6,
		relheight = 0.3)

# widget displaying place info of rect
label = Label(root)

# place a widget in a specific
# position in the parent widget.
label.place(rely = 0.6)

# get a info of the place
label['text'] = rect.place_info()

# start the GUI
root.mainloop()
