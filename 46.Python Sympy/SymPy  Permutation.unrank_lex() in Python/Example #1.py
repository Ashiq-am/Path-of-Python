# Python code explaining
# SymPy.Permutation.unrank_lex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.permutations import Permutation

# Using from sympy.combinatorics.permutations.Permutation.unrank_lex() method

# creating Permutation
a = Permutation([[2, 0], [3, 1]])

b = Permutation([1, 3, 5, 4, 2, 0])

size = 2
rank = 5

print ("Permutation a - unrank_lex form : ", a.unrank_lex(size, rank))
print ("Permutation b - unrank_lex form : ", b.unrank_lex(size, 2))
