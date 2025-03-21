# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calender
cal = Calendar(root, selectmode = 'day', year = 2020, month = 5, day = 22)

cal.pack(pady = 20)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())

# Add Button and Label
Button(root, text = "Get Date",
	command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Excecute Tkinter
root.mainloop()
