# Python code explaining
# SymPy.Permutation.next_lex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.next_lex() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])


print ("Permutation a - next_lex form : ", a.next_lex())
print ("Permutation b - next_lex form : ", b.next_lex())
