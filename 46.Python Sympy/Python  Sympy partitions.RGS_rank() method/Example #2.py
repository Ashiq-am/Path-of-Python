# import sympy and RGS_unrank
from sympy.combinatorics.partitions import RGS_rank
from sympy import *


x, y = symbols('x y')

# Using sympy.combinatorics.partitions.RGS_rank method
gfg = RGS_rank([2, 1, 5, 1, 0, 7])

print(gfg)
