# import sympy and Circle, Ellipse, Point, symbols
from sympy import Circle, Ellipse, Point, symbols

p = Point(3, 8)
a, b = symbols('a b')

# using director_circle() method
directorCircle = Ellipse(p, a, b).director_circle()

print(directorCircle)
