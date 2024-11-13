# import sympy and Circle, Ellipse, Point
from sympy import Circle, Ellipse, Point

p = Point(3, 8)

# using director_circle() method
directorCircle = Ellipse(p, 7, 9).director_circle()

print(directorCircle)
