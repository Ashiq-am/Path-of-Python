# Import package and it's modules
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("GeekForGeeks")

# Set geometry (widthxheight)
root.geometry('400x400')

# Entry Box
text = Entry(root, width = 30, bg = 'White')
text.pack(pady = 10)

# Execute Tkinter
root.mainloop()
