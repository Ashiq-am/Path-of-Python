# Python3 program to demonstrate the
# error in function modf()

# This will import math module
from math import modf

lst = [3.12, -5.14, 13.25, -5.21]
tpl = (33.12, -15.25, 3.15, -31.2)


# modf() function on elements of list
print("modf() on First list element : ", modf(lst[0]))
print("modf() on third list element : ", modf(lst[2]))

# modf() function on elements of tuple
print("modf() on Second tuple element : ", modf(tpl[1]))
print("modf() on Fourth tuple element : ", modf(tpl[3]))
