# import sympy and Relational
from sympy.combinatorics.partitions import Partition
from sympy import *

x, y = symbols('x y')

# Using from sympy.combinatorics.Partition.from_rgs() method
gfg = Partition.from_rgs([0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 0, 1, 5],
						list('abcdefghijklm'))

print(gfg)
