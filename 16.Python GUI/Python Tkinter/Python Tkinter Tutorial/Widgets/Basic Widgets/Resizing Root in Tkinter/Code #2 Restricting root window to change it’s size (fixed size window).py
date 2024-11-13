# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.title('Resizable')
root.geometry('250x100')

Label(root, text = 'It\'s non-resizable').pack(side = TOP, pady = 10)

# Restricting root window to change
# it's size according to user's need
root.resizable(0, 0)

mainloop()
