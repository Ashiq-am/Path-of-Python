# Python code explaining
# SymPy.Permutation.rmul()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.rmul() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - rmul form : ", a.rmul(b))
print ("Permutation b - rmul form : ", b.rmul(a))
