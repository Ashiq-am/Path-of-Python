# Python code explaining
# SymPy.Permutation.next_trotterjohnson()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.next_trotterjohnson() method

# creating Permutation
a = Permutation([[2, 4, 0],
				[3, 1, 2],
				[1, 5, 6]])


print ("Permutation a - next_trotterjohnson form : ", a.next_trotterjohnson())
