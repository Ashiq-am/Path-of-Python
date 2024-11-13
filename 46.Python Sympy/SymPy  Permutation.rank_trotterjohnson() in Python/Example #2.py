# Python code explaining
# SymPy.Permutation.rank_trotterjohnson()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.rank_trotterjohnson() method

# creating Permutation
a = Permutation([[2, 4, 0],
				[3, 1, 2],
				[1, 5, 6]])


print ("Permutation a - rank_trotterjohnson form : ", a.rank_trotterjohnson())
