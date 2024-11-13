import unittest
from .. import app

class TestSum(unittest.TestCase):

	def test_area(self):
		sq = app.Square(2)
		self.assertEqual(sq.area(), 4,
			f'Area is shown {sq.area()} rather than 9')

	def test_area_negative(self):
		sq = app.Square(-3)
		self.assertEqual(sq.area(), -1,
			f'Area is shown {sq.area()} rather than -1')

	def test_perimeter(self):
		sq = app.Square(5)
		self.assertEqual(sq.perimeter(), 20,
			f'Perimeter is {sq.perimeter()} rather than 20')

	def test_perimeter_negative(self):
		sq = app.Square(-6)
		self.assertEqual(sq.perimeter(), -1,
			f'Perimeter is {sq.perimeter()} rather than -1')

if __name__ == '__main__':
	unittest.main()
