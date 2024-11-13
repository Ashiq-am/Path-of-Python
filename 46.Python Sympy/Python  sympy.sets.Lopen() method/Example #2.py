# import sympy
from sympy.sets import Interval

# Use sympy.sets.Lopen() method
gfg = Interval.Lopen(0, 3)
print(gfg)

print(gfg.contains(0))
