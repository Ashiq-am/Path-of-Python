''''''


"""This method is used to ask the user about doing a particular task again or not"""

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.askretrycancel("Application", "try again?")

top.mainloop()