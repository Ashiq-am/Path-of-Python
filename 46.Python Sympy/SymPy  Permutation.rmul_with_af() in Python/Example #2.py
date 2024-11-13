# Python code explaining
# SymPy.Permutation.rmul_with_af()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.rmul_with_af() method

# creating Permutation
a = Permutation([[2, 4, 0],
				[3, 1, 2],
				[1, 5, 6]])


print ("Permutation a - rmul_with_af form : ", a.rmul_with_af(a))
