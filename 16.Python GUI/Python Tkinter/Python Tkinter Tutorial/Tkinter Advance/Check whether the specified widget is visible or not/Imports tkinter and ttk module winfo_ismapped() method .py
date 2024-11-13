# Imports tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import time

# toplevel window
root = Tk()

def forget(widget):
	widget.forget()
	print("After Forget method called. Is widget mapped? = ",
							bool(widget.winfo_ismapped()))

def retrieve(widget):
	widget.pack()
	print("After retrieval of widget. Is widget mapped? = ",
								bool(widget.winfo_exists()))

# Button widgets
b1 = Button(root, text = "Btn 1")
b1.pack()

# This is used to make widget invisible
b2 = Button(root, text = "Btn 2", command = lambda : forget(b1))
b2.pack()

# This will retrieve widget
b3 = Button(root, text = "Btn 3", command = lambda : retrieve(b1))
b3.pack()

# infinite loop, interrupted by keyboard or mouse
mainloop()
