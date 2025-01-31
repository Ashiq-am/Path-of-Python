class Shape:
	def area(self):
		raise NotImplementedError("Subclasses must Implement area()")


class Rectangle(Shape):
	def __init__(self, length, width):
		self.width = width
		self.length = length

	def area(self):
		print(f"The Area of Rectangle is {self.length*self.width}")


class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)

	def area(self):
		print(f"The Area of Rectangle is {self.length ** 2}")


# Creating Objects of class
Rect = Rectangle(3, 4)
my_sqre = Square(4)

Rect.area()
my_sqre.area()
