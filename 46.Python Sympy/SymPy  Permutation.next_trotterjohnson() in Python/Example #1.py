# Python code explaining
# SymPy.Permutation.next_trotterjohnson()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from
# sympy.combinatorics.permutations.Permutation.next_trotterjohnson() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - next_trotterjohnson form : ", a.next_trotterjohnson())
print ("Permutation b - next_trotterjohnson form : ", b.next_trotterjohnson())
