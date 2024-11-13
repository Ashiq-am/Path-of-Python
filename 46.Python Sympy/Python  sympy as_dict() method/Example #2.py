# import sympy and IntegerPartition
from sympy.combinatorics.partitions import IntegerPartition
from sympy import *

# Using sympy.combinatorics.partitions.IntegerPartition().as_dict() method
gfg = IntegerPartition([1] + 2 * [2, 3] + 4 * [4] + 5 * [5]).as_dict()

print(gfg)
