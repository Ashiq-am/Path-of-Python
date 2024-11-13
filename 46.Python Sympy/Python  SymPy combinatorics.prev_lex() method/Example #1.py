# import sympy and IntegerPartition
from sympy.combinatorics.partitions import IntegerPartition
from sympy import *

# Using sympy.combinatorics.partitions.IntegerPartition().prev_lex() method
gfg = IntegerPartition([1, 2, 3])

print(gfg.prev_lex())
