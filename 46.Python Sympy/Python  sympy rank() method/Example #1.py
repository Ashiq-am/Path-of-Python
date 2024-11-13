# import sympy and Partition
from sympy.combinatorics.partitions import Partition
from sympy import *

x, y = symbols('x y')

# Using sympy.combinatorics.partitions.Partition().rank method
gfg = Partition([1, 2], [4, 5, 6], [-12, -11])

print(gfg.rank)
