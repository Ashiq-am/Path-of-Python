# Python code explaining
# SymPy.Permutation.cardinality()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.cardinality() method

# creating Permutation
a = Permutation([[2, 4, 0],
				[3, 1, 2],
				[1, 5, 6]])


print ("Permutation a - cardinality form : ", a.cardinality)
