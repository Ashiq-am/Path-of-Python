# Import Module
from tkinter import *

# Create Objects
root = Tk()

# Create Bitmaps List
bitmaps = ["error",
		"gray75",
		"gray50",
		"gray25",
		"gray12",
		"hourglass",
		"info",
		"questhead",
		"question",
		"warning"]

# Iterate through all bitmap list
for bit in bitmaps:
	Button(root, relief=RAISED, bitmap=bit).pack(pady=10)

# Execute Tkinter
root.mainloop()
