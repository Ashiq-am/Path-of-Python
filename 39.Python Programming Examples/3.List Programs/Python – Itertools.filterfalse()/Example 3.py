# Python program to demonstrate
# the working of filterfalse
import itertools
from itertools import filterfalse

li = [2, 4, 5, 7, 8, 10, 20]

# Slicing the list
print(list(itertools.filterfalse(lambda x: x % 2 == 0, li)))
