class Person:

	def __init__(self):
		self._name = None

	def name(self):
		print('name function called')
		return self._name

	# for read-only attribute
	n = property(name, None)

p = Person()

setattr(p, 'n', 'rajav')
