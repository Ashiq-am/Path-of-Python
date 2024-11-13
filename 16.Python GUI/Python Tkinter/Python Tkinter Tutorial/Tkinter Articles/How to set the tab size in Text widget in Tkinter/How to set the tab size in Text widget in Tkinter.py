# Import Module
from tkinter import *
import tkinter.font as tkfont

# Create Object
root = Tk()

# Set Geometry
root.geometry("400x400")

# Add Text Box
text = Text(root)
text.pack()

# Set Font
font = tkfont.Font(font=text['font'])

# Set Tab size
tab_size = font.measure('		 ')
text.config(tabs=tab_size)

# Execute Tkinter
root.mainloop()
