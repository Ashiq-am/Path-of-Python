# Python program to demonstrate
# the working of filterfalse
import itertools
from itertools import filterfalse

# function is a None
for i in filterfalse(None, range(20)):
    print(i)

li = [2, 4, 5, 7, 8, 10, 20]

# Slicing the list
print(list(itertools.filterfalse(None, li)))
