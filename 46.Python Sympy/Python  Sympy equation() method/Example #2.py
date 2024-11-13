# import sympy, Point and Circle
from sympy import Point, Circle

# using Circle()
c3 = Circle(Point(1, 2), 5)
c4 = c3.equation()

print(c4)
