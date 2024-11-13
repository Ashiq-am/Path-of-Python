# Import Required Library
from tkinter import *
from tkcalendar import Calendar
import datetime

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calender
cal = Calendar(root, selectmode='day',
			year=2020, month=5,
			day=22)

cal.pack(pady=20)

frame1 = Frame()
frame2 = Frame()

frame1.pack()
frame2.pack()

# making label
Label(frame1, text="Days", bd=1, bg="white", width=20,
	relief="solid", font="italic 10 bold").pack(side=LEFT)

# input for days
days = Spinbox(frame1, from_=0, to=10000000, font="italic 10")
days.pack(pady=20, padx=10)

# making buttons
Button(frame2, text="Add Days", font="italic 15").pack(side=LEFT)
Button(frame2, text="Subtract Days", font="italic 15").pack(padx=10)

# making label
converted_date = Label(text="Date: ", bd=2, bg="white", relief="solid",
					font="italic 10 bold", width=30)
converted_date.pack(pady=20)

# Excecute Tkinter
root.mainloop()
