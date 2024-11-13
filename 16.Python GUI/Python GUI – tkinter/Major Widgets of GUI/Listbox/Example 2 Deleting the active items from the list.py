# !/usr/bin/python3

from tkinter import *

top = Tk()

top.geometry("5000x5000")

lbl = Label(top, text="A list of favourite countries...")

listbox = Listbox(top)

listbox.insert(1, "ADIBA")

listbox.insert(2, "Rommel Hassan")

listbox.insert(3, "ASHIQ")

listbox.insert(4, "RIFFAT ISLAM")

# this button will delete the selected item from the list

btn = Button(top, text="delete", command=lambda listbox=listbox: listbox.delete(ANCHOR))

lbl.pack()

listbox.pack()

btn.pack()
top.mainloop()