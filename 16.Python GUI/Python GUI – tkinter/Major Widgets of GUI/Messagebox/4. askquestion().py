''''''

'''This method is used to ask some question to the user which can be answered in yes or no'''

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.askquestion("Confirm", "Are you sure?")
top.mainloop()  