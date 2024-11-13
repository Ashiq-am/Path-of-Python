# Slower
class SomeClass:
	...
	def method(self):
		for x in s:
			op(self.value)
# Faster
class SomeClass:
	...
	def method(self):
		value = self.value
		for x in s:
			op(value)
