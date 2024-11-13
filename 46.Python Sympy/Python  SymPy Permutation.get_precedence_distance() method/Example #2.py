# Python code explaining
# SymPy.Permutation.get_precedence_distance()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.get_precedence_distance() method

# creating Permutation
a = Permutation([[2, 4, 0],
                 [7, 1, 3],
                 [8, 5, 6]])

b = Permutation([[8, 4, 0],
                 [2, 7, 0],
                 [1, 6, 7]])

print("a get_precedence_distance form b : ", a.get_precedence_distance(b))
