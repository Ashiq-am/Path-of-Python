# Python code explaining
# SymPy.next_lex()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import IntegerPartition

# Using from sympy.combinatorics.partitions.Partition.next_lex() method
p = IntegerPartition([312, 121, 14, 5])

print('p : ', p)
print('\nNext Integrer : ', p.next_lex())
