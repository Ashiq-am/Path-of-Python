# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()

# setting the minimum size of the root window
root.minsize(150, 100)

# Adding widgets to the root window
Label(root, text = 'GeeksforGeeks',font =('Verdana', 15)).pack(side = TOP, pady = 10)
Button(root, text = 'Click Me !').pack(side = TOP)

mainloop()
