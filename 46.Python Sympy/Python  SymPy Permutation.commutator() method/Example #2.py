# Python code explaining
# SymPy.Permutation.commutator()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.commutator() method

# creating Permutation
a = Permutation([[2, 4, 0],
				[3, 1, 2],
				[1, 5, 6]])

# SELF COMMUTATING
print ("Permutation a - commutator form : ", a.commutator(a))
