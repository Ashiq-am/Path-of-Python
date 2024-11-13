# This imports all functions in tkinter module
from tkinter import *
from tkinter.ttk import *

# creating master window
master = Tk()


# This method is used to get the size
# of the desired widget i.e number of grids
# available in the widget
def grids(event):
    # Here, grid_size() method is used to get
    # the total number grids available in frame
    # widget
    x = f.grid_size()

    # printing (columns, rows)
    print(x)


# Frame widget, will work as
# parent for buttons widget
f = Frame(master)
f.pack()

# Button widgets
b = Button(f, text="Button")
b.grid(row=1, column=2)

c = Button(f, text="Button2")
c.grid(row=1, column=0)

# Here binding click method with mouse
master.bind("<Button-1>", grids)

# infinite loop
mainloop()
