class Shape:
	def __init__(self, color):
		self.color = color

	def area(self):
		pass

class Circle(Shape):
	def __init__(self, color, radius):
		super().__init__(color)
		self.radius = radius

	def area(self):
		return 3.14 * self.radius**2

class Square(Shape):
	def __init__(self, color, side_length):
		super().__init__(color)
		self.side_length = side_length

	def area(self):
		return self.side_length**2

# Usage
circle = Circle("Red", 5)
square = Square("Blue", 4)
print(circle.area())
print(square.area())
