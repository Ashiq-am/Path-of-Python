# Python code explaining
# SymPy.Permutation.length()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.length() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - length form : ", a.length())
print ("Permutation b - length form : ", b.length())
