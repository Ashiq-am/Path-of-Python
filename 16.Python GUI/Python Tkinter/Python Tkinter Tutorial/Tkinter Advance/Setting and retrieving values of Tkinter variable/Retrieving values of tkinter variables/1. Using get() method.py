# importing tkinter module
from tkinter import *

# creating Tk() variable
# required by Tkinter classes
master = Tk()

# Tkinter variables
# Giving user defined names to each variables
# so that variables can be modified easily
intvar = IntVar(master, name ="int")
strvar = StringVar(master, name ="str")
boolvar = BooleanVar(master, name ="bool")
doublevar = DoubleVar(master, name ="float")

# Setting values of variables
# using setvar() method
master.setvar(name ="int", value = 100)
master.setvar(name ="str", value ="GFG")
master.setvar(name ="bool", value = False)
master.setvar(name ="float", value = 1.236)

# getting values of each variables using get() method
print("Value of IntVar()", intvar.get())
print("Value of StringVar()", strvar.get())
print("Value of BooleanVar()", boolvar.get())
print("Value of DoubleVar()", doublevar.get())
