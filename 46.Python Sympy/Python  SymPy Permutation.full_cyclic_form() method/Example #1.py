# Python code explaining
# SymPy.Permutation.full_cyclic_form()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.full_cyclic_form() method

# creating Permutation
a = Permutation([2, 0, 3, 1, 5, 4])

b = Permutation([3, 1, 2, 5, 4, 0])


print ("Permutation a - full_cyclic_form form : ", a.full_cyclic_form)
print ("Permutation b - full_cyclic_form form : ", b.full_cyclic_form)
