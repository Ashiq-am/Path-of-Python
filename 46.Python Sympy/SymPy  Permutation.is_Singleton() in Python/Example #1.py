# Python code explaining
# SymPy.Permutation.is_Singleton()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.is_Singleton() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([0])


print ("Permutation a - is_Singleton form : ", a.is_Singleton)
print ("Permutation b - is_Singleton form : ", b.is_Singleton)
