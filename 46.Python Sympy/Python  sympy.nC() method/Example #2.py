# import sympy
from sympy import *
from sympy.functions.combinatorial.numbers import nC

items = [2, 1, 3, 5, 4]
k = 3
print("Value of k = {} and the items are = {}".format(k, items))

# Use sympy.nC() method
combinations = nC(items, k)

print("Combinations : {}".format(combinations))
