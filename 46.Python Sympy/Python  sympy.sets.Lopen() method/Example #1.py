# import sympy
from sympy.sets import Interval

# Use sympy.sets.Lopen() method
gfg = Interval.Lopen(0, 10)
print(gfg)

print(gfg.contains(8))
