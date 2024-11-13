class invertClass(object):
	def __init__(self, value):
		self._value = value
	def __invert__(self):
		return self._value[::-1]
	def __str__(self):
		return self._value

invrt = invertClass('Hello, George')
invertedValue = ~invrt
print(invertedValue)
