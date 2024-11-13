class Cube(SquarePrism):
	def __init__(self, side):
		super().__init__(side = side, height = side)

	def face_area(self):
		return super(SquarePrism, self).area()

	def area(self):
		return super().area()
