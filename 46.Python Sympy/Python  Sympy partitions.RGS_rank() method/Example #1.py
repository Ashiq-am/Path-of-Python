# import sympy and RGS_unrank
from sympy.combinatorics.partitions import RGS_rank
from sympy import *

x, y = symbols('x y')

# Using sympy.combinatorics.partitions.RGS_rank method
gfg = RGS_rank([1, 2, 5, 4, 2, 10])

print(gfg)
