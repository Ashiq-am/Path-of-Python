# Python code explaining
# SymPy.Permutation.commutes_with()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.commutes_with() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([3, 1, 2, 5, 4, 0])


print ("Permutation a - commutes_with form : ", a.commutes_with(b))
print ("Permutation b - commutes_with form : ", b.commutes_with(a))
