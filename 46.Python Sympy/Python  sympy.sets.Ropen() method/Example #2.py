# import sympy
from sympy.sets import Interval

# Use sympy.sets.Ropen() method
gfg = Interval.Ropen(0, 5)
print(gfg)

print(gfg.contains(5))
