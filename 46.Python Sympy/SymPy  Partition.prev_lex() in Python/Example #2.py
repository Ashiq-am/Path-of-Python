# Python code explaining
# SymPy.prev_lex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import IntegerPartition

# Using from sympy.combinatorics.partitions.Partition.prev_lex() method
p = IntegerPartition([1, 312, 121, 14,34, 56, 32])

print('p : ', p)
print('\nPrevious Integrer : ', p.prev_lex())
