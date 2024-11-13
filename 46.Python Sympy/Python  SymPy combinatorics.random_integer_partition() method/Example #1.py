# import sympy and IntegerPartition
from sympy.combinatorics.partitions import random_integer_partition
from sympy import *

# Using sympy.combinatorics.partitions.random_integer_partition() method
gfg = random_integer_partition(50)

print(gfg)
