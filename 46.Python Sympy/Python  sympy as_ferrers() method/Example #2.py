# import sympy and IntegerPartition
from sympy.combinatorics.partitions import IntegerPartition
from sympy import *

# Using sympy.combinatorics.partitions.IntegerPartition().as_ferrers() method
gfg = IntegerPartition([1] + [2, 3] + [4] + [5]).as_ferrers(char ='$')

print(gfg)
