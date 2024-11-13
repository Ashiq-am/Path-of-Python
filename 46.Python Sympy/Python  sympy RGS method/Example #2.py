# import sympy and Relational
from sympy.combinatorics.partitions import Partition
from sympy import *

x, y = symbols('x y')

# Using from sympy.combinatorics.partitions.Partition() method
gfg = Partition([3], [1, 91], [2], [6])

print(gfg.RGS)
