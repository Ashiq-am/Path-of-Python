# Python code explaining
# SymPy.Permutation.rmul_with_af()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.rmul_with_af() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - rmul_with_af form : ", a.rmul_with_af(b))
print ("Permutation b - rmul_with_af form : ", b.rmul_with_af(a))
