# Python code explaining
# SymPy.Permutation.is_odd()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.is_odd() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - is_odd form : ", a.is_odd)
print ("Permutation b - is_odd form : ", b.is_odd)
