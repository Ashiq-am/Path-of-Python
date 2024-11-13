# Python code explaining
# SymPy.Permutation.is_Identity()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.is_Identity() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])

print ("Permutation a - is_Identity form : ", a.is_Identity)
print ("Permutation b - is_Identity form : ", b.is_Identity)
