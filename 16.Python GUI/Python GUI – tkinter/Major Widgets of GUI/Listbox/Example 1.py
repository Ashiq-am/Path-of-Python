# !/usr/bin/python3

from tkinter import *

top = Tk()

top.geometry("200x250")

lbl = Label(top, text="A list of favourite countries...")

listbox = Listbox(top)

listbox.insert(1, "Bangladesh")

listbox.insert(2, "USA")

listbox.insert(3, "Japan")

listbox.insert(4, "Australia")

lbl.pack()
listbox.pack()

top.mainloop()