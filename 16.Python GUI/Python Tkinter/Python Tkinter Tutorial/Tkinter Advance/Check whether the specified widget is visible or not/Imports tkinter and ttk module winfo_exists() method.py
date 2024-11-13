# Imports tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# toplevel window
root = Tk()


def dest(widget):
    widget.destroy()
    print("Destroy method called. Widget exists? = ",
          bool(widget.winfo_exists()))


def exist(widget):
    print("Checking for existance = ", bool(widget.winfo_exists()))


# Button widgets
b1 = Button(root, text="Btn 1")
b1.pack()

# This is used to destroy widget
b2 = Button(root, text="Btn 2", command=lambda: dest(b1))
b2.pack()

# This is used to check existance of the widget
b3 = Button(root, text="Btn 3", command=lambda: exist(b1))
b3.pack()

# infinite loop, interrupted by keyboard or mouse
mainloop()
