# Python code explaining
# SymPy.Permutation.unrank_nonlex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.unrank_nonlex() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - unrank_nonlex form : ", a.unrank_nonlex(2, 5))
print ("Permutation b - unrank_nonlex form : ", b.unrank_nonlex(1, 6))
