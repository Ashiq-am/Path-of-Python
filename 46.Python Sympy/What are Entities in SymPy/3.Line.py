# importing packages
from sympy.geometry import Point, Line

# creating two points
p1, p2 = Point(1, 2), Point(2, 0)
line1 = Line(p1, p2)
print(line1)

# creating two points
line2 = Line(Point(2, 4), Point(6, 2))
print(line2)

# intersection point of two lines
print(line1.intersection(line2))

# Angle between the two lines
print('Angle between two lines is : \
' + str(line1.angle_between(line2)))
