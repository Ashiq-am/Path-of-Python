# importing the installed library
import sys
from recordclass import recordclass

Point = recordclass('Point', ('x', 'y', 'z'))

Coordinates = Point(3, 0, 1)
print(sys.getsizeof(Coordinates))
