# Python code explaining
# SymPy.Permutation.cardinality()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.cardinality() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - cardinality form : ", a.cardinality)
print ("Permutation b - cardinality form : ", b.cardinality)
