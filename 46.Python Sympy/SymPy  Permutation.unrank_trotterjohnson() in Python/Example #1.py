# Python code explaining
# SymPy.Permutation.unrank_trotterjohnson()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.unrank_trotterjohnson() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])

size = 3

rank = 5

print ("Permutation a - unrank_trotterjohnson form : ", a.unrank_trotterjohnson(size, rank))
print ("Permutation b - unrank_trotterjohnson form : ", b.unrank_trotterjohnson(5, rank))
