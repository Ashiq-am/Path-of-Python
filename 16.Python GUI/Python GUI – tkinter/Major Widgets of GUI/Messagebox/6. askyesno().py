''''''


'''This method is used to ask the user about some action to which, the user can answer in yes or no'''

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.askyesno("Application", "Got It?")
top.mainloop()  