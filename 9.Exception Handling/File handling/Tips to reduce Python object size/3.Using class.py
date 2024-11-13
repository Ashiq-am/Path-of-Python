import sys

class Point:

	# defining the coordinate variables
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

Coordinates = Point(3, 0, 1)
print(sys.getsizeof(Coordinates))
