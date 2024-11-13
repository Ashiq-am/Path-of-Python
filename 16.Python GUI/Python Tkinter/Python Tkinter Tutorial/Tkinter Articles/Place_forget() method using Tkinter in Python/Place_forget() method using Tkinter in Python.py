# Imports everything from tkinter
# and ttk module
from tkinter import *
from tkinter.ttk import *

# toplevel window
root = Tk()

# setting window size
root.geometry("150x100")

# label widget
label = Label(root, text="LABEL")

# place in the window
label.place(relx=0.4, y=5)

# button widgets
# In command attribute of Button,
# place_forget() method is passed
# in the lambda function to temporarily
# hide the label
b1 = Button(root, text = "hide text",command = lambda: label.place_forget())

b1.place(relx = 0.3, y = 30)

# the label is placed again
b2 = Button(root, text = "retrieve text",command = lambda: label.place( relx = 0.4))

b2.place(relx = 0.3, y = 50)

# Start the GUI
root.mainloop()
