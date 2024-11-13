# importing module
from tkinter import *

# main container
root = Tk()

# frame
frame = Frame(root, relief = 'sunken',
			bd = 1, bg = 'white')
frame.pack(fill = 'both', expand = True,
		padx = 10, pady = 10)

# container content
lable = Label(frame, text = 'GeeksForGeeks.org!',
			width = 45, height = 10, bg = "black",
			fg = "white")
lable.pack()

root.mainloop()
