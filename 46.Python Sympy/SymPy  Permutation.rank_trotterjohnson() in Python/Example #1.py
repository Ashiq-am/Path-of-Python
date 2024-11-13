# Python code explaining
# SymPy.Permutation.rank_trotterjohnson()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.rank_trotterjohnson() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - rank_trotterjohnson form : ", a.rank_trotterjohnson())
print ("Permutation b - rank_trotterjohnson form : ", b.rank_trotterjohnson())
