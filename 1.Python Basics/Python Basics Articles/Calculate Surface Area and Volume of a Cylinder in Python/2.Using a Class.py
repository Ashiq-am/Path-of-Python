import math

class Cylinder:
	def __init__(self, radius, height):
		self.radius = radius
		self.height = height

	def surface_area(self):
		return 2 * math.pi * self.radius**2 + 2 * math.pi * self.radius * self.height

	def volume(self):
		return math.pi * self.radius**2 * self.height

# Example usage:
cylinder = Cylinder(5, 10)
print(f"Surface Area: {cylinder.surface_area()}")
print(f"Volume: {cylinder.volume()}")
