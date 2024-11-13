# import sympy, Interval
from sympy import Interval

# Using sympy.Interval().intersect() method
gfg = Interval(0.5, 0.9).intersect(Interval(0.7, 1.2))

print(gfg)
