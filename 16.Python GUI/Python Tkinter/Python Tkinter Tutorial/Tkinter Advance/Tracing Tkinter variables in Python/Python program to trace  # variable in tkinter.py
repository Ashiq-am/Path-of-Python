# Python program to trace
# variable in tkinter


from tkinter import *


root = Tk()

my_var = StringVar()

# defining the callback function (observer)
def my_callback(var, indx, mode):
    print ("Traced variable {}".format(my_var.get()))

my_var.trace_add('write', my_callback)

Label(root, textvariable = my_var).pack(padx = 5, pady = 5)

Entry(root, textvariable = my_var).pack(padx = 5, pady = 5)

root.mainloop()
