# import sympy and Permutation
from sympy.combinatorics.permutations import Permutation
from sympy import *

Permutation.print_cyclic = False

# Using sympy.combinatorics.partitions.Permutation().array_form method
gfg = Permutation([[1, 2], [3, 4], [5]])

print(gfg.array_form)
