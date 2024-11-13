class Shape:
	def __init__(self, color):
		self.color = color

	def draw(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		super().__init__("Red")
		self.radius = radius

	def draw(self):
		return f"Drawing a red circle with radius {self.radius} units."

# Creating an instance of the derived class
my_circle = Circle(5)

# Accessing attributes and methods from both base and derived classes
print(f"Color: {my_circle.color}, Draw: {my_circle.draw()}")
