class Square(object):
	def __init__(self, number = 2):
		self._number = number

	def square(self):
		return self._number**2

s = Square()
print('Number: % i' % s._number)
print('Square: % i' % s.square())
