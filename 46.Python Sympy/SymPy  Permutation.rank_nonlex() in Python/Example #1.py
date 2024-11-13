# Python code explaining
# SymPy.Permutation.rank_nonlex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.rank_nonlex() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - rank_nonlex form : ", a.rank_nonlex())
print ("Permutation b - rank_nonlex form : ", b.rank_nonlex())
