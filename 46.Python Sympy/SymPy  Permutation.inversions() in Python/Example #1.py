# Python code explaining
# SymPy.Permutation.inversions()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.inversions() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - inversions form : ", a.inversions())
print ("Permutation b - inversions form : ", b.inversions())
