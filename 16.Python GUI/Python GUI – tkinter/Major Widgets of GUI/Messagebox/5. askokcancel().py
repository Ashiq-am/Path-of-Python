''''''


'''This method is used to confirm the user's action regarding some application activity'''

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.askokcancel("Redirect", "Redirecting you to www.javatpoint.com")
top.mainloop() 