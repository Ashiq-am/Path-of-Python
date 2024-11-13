# Python code explaining
# SymPy.Permutation.unrank_trotterjohnson()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.unrank_trotterjohnson() method

# creating Permutation
a = Permutation([[2, 4, 0],
				[3, 1, 2],
				[1, 5, 6]])


print ("Permutation a - unrank_trotterjohnson form : ", a.unrank_trotterjohnson(4, 8))
