# Python code explaining
# SymPy.Permutation.cyclic_form()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.cyclic_form() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([3, 1, 2, 5, 4, 0])


print ("Permutation a - cyclic_form form : ", a.cyclic_form)
print ("Permutation b - cyclic_form form : ", b.cyclic_form)
