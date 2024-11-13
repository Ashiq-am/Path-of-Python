class inPlace(object):
	def __init__(self, value):
		self._value = value
	def __iadd__(self, other):
		self._value = self._value + other._value
		return self._value
	def __str__(object):
		return self._value

inP1 = inPlace(5)
inP2 = inPlace(3)
inP1 += inP2
print(inP1)
