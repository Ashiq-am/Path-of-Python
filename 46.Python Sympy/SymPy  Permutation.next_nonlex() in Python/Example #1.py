# Python code explaining
# SymPy.Permutation.next_nonlex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.next_nonlex() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - next_nonlex form : ", a.next_nonlex())
print ("Permutation b - next_nonlex form : ", b.next_nonlex())
