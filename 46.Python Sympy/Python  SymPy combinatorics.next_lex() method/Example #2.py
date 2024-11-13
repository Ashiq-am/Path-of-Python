# import sympy and IntegerPartition
from sympy.combinatorics.partitions import IntegerPartition
from sympy import *

# Using sympy.combinatorics.partitions.IntegerPartition().next_lex() method
gfg = IntegerPartition([1, 2, 3, 4, 3, 2, 1])

print(gfg.next_lex())
