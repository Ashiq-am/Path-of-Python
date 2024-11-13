# Class to represent a rectangle and calculate its area
class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_area(self):
		return self.length * self.width

# Example usage:
rectangle_instance = Rectangle(5, 8)
result = rectangle_instance.calculate_area()
print(f"Area of Rectangle: {result}")
