# Python code explaining
# SymPy.Permutation.mul_inv()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.mul_inv() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - mul_inv form : ", a.mul_inv(a))
print ("Permutation b - mul_inv form : ", b.mul_inv(b))
