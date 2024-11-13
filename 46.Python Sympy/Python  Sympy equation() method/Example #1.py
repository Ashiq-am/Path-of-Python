# import sympy, Point and Circle
from sympy import Point, Circle

# using Circle()
c1 = Circle(Point(0, 0), 5)
c2 = c1.equation()

print(c2)
