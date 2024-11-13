# Python code explaining
# SymPy.from_inversion_vector()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.from_inversion_vector() method

# creating vectors
a = [1, 0, 0, 0]

b = [6, 5, 4, 3, 0, 0 ]

# inversion forms
print ("vector a - from_inversion_vector form : ",
	Permutation.from_inversion_vector(a))
print ("vector b - from_inversion_vector form : ",
	Permutation.from_inversion_vector(b))
