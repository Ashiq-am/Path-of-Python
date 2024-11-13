# This will import tkinter and ttk
from tkinter import *
from tkinter import ttk

root = Tk()

# This will set the geometry to 200x100
root.geometry('200x100')

text1 = StringVar()
text2 = StringVar()

# These text are used to set initial
# values of Checkbutton to off
text1.set('OFF')
text2.set('OFF')

chkbtn1 = ttk.Checkbutton(root, textvariable = text1, variable = text1,
						offvalue = 'GFG Not Selected',
						onvalue = 'GFG Selected')

chkbtn1.pack(side = TOP, pady = 10)
chkbtn2 = ttk.Checkbutton(root, textvariable = text2, variable = text2,
						offvalue = 'GFG Average',
						onvalue = 'GFG Good')
chkbtn2.pack(side = TOP, pady = 10)

root.mainloop()
