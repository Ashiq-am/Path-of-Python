# Python code explaining
# SymPy.Permutation.get_positional_distance()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.get_positional_distance() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([3, 1, 2, 5, 4, 0])

c = Permutation([0, 1, 3, 4, 5, 2])

print ("a - get_positional_distance form b: ", a.get_positional_distance(b))
print ("b - get_positional_distance form c: ", b.get_positional_distance(c))
