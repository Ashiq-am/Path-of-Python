class unaryOp(object):
	def __init__(self, value):
		self._value = value
	def __neg__(self):
		print('__neg__ magic method')
		return(-self._value)

up = unaryOp(5)
print(-up)
