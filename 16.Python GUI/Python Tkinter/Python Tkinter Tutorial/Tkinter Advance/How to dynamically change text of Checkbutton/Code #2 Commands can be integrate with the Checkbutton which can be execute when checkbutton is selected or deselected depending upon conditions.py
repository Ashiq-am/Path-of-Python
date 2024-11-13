# Importing tkinter, ttk and
# _show method to display
# pop-up message window
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import _show

root = Tk()
root.geometry('200x100')

text1 = StringVar()
text1.set('OFF')

# This function is used to display
# the pop-up message
def show(event):
	string = event.get()
	_show('Message', 'You selected ' + string)

chkbtn1 = ttk.Checkbutton(root, textvariable = text1, variable = text1,
						offvalue = 'GFG Good',
						onvalue = 'GFG Great',
						command = lambda : show(text1))
chkbtn1.pack(side = TOP, pady = 10)

root.mainloop()
