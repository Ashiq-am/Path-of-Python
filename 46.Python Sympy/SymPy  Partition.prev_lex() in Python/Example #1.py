# Python code explaining
# SymPy.prev_lex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import IntegerPartition

# Using from sympy.combinatorics.partitions.Partition.prev_lex() method
p = IntegerPartition([312, 121, 14, 5])

print('p : ', p)
print('\nPrevious Integrer : ', p.prev_lex())
