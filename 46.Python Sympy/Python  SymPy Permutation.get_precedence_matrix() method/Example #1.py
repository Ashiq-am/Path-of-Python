# Python code explaining
# SymPy.Permutation.get_precedence_matrix()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.get_precedence_matrix() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([3, 1, 2, 5, 4, 0])

print ("a - get_precedence_matrix : \n", a.get_precedence_matrix())
print ("b - get_precedence_matrix : \n", b.get_precedence_matrix())
