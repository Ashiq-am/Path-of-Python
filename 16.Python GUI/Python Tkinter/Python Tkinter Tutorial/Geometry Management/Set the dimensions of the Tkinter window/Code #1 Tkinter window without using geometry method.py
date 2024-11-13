# importing only those functions which are needed
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button

# creating tkinter window
root = Tk()

button = Button(root, text = 'Geeks')
button.pack(side = TOP, pady = 5)

mainloop()
