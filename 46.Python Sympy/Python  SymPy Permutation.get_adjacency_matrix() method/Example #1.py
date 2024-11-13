# Python code explaining
# SymPy.Permutation.get_adjacency_matrix()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.get_adjacency_matrix() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([3, 1, 2, 5, 4, 0])

print ("a - get_adjacency_matrix : \n", a.get_adjacency_matrix())
print ("b - get_adjacency_matrix : \n", b.get_adjacency_matrix())
