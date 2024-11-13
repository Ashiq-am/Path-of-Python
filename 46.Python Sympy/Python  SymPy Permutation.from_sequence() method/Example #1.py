# Python code explaining
# SymPy.from_sequence()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.from_sequence() method

# creating vectors
a = [1, 0, 0, 0]

b = [6, 5, 4, 3, 0, 0 ]

# inversion forms
print ("vector a - from_sequence form : \n", Permutation.from_sequence(a))
print ("vector b - from_sequence form : \n", Permutation.from_sequence(b))
