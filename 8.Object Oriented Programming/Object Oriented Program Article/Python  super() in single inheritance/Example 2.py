class Cube(Square):
	def area(self):
		return super().area() * 6

	def volume(self):
		return super().area() * self.side()
