# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()

# Fixing the size of the root window.
# No one can now expand the size of the
# root window than the specified one.
root.maxsize(200, 200)

# Adding widgets to the root window
Label(root, text = 'GeeksforGeeks',font =('Verdana', 15)).pack(side = TOP, pady = 10)

Button(root, text = 'Click Me !').pack(side = TOP)

mainloop()
