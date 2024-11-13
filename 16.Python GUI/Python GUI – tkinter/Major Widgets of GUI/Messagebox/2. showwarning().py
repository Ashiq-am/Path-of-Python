''''''

'''This method is used to display the warning to the user'''

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
messagebox.showwarning("warning", "Warning")

top.mainloop()  