''''''


"""The showinfo() messagebox is used where we need to show some relevant information to the user."""

from tkinter import *

from tkinter import messagebox

top = Tk()

top.geometry("100x100")

messagebox.showinfo("information", "Information")

top.mainloop()  