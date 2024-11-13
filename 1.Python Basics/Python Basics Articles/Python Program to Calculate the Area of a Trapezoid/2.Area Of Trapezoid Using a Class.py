class Trapezoid:
	def __init__(self, base1, base2, height):
		self.base1 = base1
		self.base2 = base2
		self.height = height

	def calculate_area(self):
		return (self.base1 + self.base2) / 2 * self.height

# Driver code
trapezoid_instance = Trapezoid(5, 9, 4)
result = trapezoid_instance.calculate_area()
print(f"Area of Trapezoid: {result}")
