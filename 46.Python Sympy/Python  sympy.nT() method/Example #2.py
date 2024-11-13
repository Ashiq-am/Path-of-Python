# import sympy
from sympy import *
from sympy.functions.combinatorial.numbers import nT

items = [1, 3, 2, 5, 4]
k = 3
print("Value of k = {} and the items are = {}".format(k, items))

# Use sympy.nT() method
partitions = nT(items, k)

print("Partitions : {}".format(partitions))
