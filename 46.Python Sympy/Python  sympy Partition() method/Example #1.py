# import sympy and Relational
from sympy.combinatorics.partitions import Partition
from sympy import *

x, y = symbols('x y')

# Using from sympy.combinatorics.partitions.Partition() method
gfg = Partition([1, 2], [4, 5, 6], [-12, -11])

print(gfg.members)
