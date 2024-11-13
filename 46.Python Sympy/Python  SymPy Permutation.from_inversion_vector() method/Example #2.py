# Python code explaining
# SymPy.from_inversion_vector()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.from_inversion_vector() method

# creating vector
a = [2, 3, 1, 0]

# inverted vector of a
print ("vector a - from_inversion_vector form : ",
	Permutation.from_inversion_vector(a))
