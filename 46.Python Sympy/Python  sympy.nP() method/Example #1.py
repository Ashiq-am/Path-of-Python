# import sympy
from sympy import *
from sympy.functions.combinatorial.numbers import nP

items = "abca"
k = 3
print("Value of k = {} and the items are = {}".format(k, items))

# Use sympy.nP() method
permutations = nP(items, k)

print("Permutation : {}".format(permutations))
