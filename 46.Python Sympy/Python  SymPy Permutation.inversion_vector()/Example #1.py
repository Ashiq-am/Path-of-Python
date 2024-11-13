# Python code explaining
# SymPy.Permutation.inversion_vector()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.inversion_vector() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - inversion_vector form : ", a.inversion_vector())
print ("Permutation b - inversion_vector form : ", b.inversion_vector())
