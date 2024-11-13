''''''


'''This method is used to display the error message to the user'''

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.showerror("error", "Error")
top.mainloop()  