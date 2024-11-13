# Python code explaining
# SymPy.Permutation.commutator()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.commutator() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - commutator form : ", a.commutator(b))
print ("Permutation b - commutator form : ", b.commutator(a))
