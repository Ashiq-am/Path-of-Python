# import sympy
from sympy.sets import Interval

# Use sympy.sets.open() method
gfg = Interval.open(0, 5)
print(gfg)

print(gfg.contains(4))
