# Python code explaining
# SymPy.Permutation.is_Empty()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.is_Empty() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - is_Empty form : ", a.is_Empty)
print ("Permutation b - is_Empty form : ", b.is_Empty)
