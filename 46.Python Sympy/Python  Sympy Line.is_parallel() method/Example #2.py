# import sympy and Point, Line
from sympy import Point, Line

p1, p2 = Point(0, 0), Point(1, 1)
p3, p4 = Point(3, 4), Point(6, 6)

l1, l2 = Line(p1, p2), Line(p3, p4)

# using is_parallel() method
isParallel = Line.is_parallel(l1, l2)

print(isParallel)
