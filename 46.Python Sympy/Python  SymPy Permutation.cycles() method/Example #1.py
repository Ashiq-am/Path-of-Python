# Python code explaining
# SymPy.Permutation.cycles()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.cycles() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([3, 1, 2, 5, 4, 0])


print ("Permutation a - cycles form : ", a.cycles)
print ("Permutation b - cycles form : ", b.cycles)
