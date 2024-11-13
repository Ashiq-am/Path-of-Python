# import sympy and IntegerPartition
from sympy.combinatorics.partitions import IntegerPartition
from sympy import *

# Using sympy.combinatorics.partitions.IntegerPartition().conjugate method
gfg = IntegerPartition([1, 2, 3])

print(gfg.conjugate)
