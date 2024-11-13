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
		return 3.14 * self.radius ** 2

# Creating instances
generic_shape = Shape("Red")
circle_instance = Circle("Blue", 5)

# Accessing attributes and methods
print(generic_shape.color)
print(circle_instance.color)
print(circle_instance.radius)
print(circle_instance.area())
