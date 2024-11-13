# import sympy and RGS_unrank
from sympy.combinatorics.partitions import RGS_unrank
from sympy import *

x, y = symbols('x y')

# Using sympy.combinatorics.partitions.RGS_unrank method
gfg = RGS_unrank(51, 8)

print(gfg)
