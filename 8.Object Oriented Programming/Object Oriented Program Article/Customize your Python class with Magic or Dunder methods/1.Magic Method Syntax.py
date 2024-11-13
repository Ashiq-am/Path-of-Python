class EquivalenceClass(object):
	def __eq__(self, other):
		return type(self) == type(other)

print(EquivalenceClass() == EquivalenceClass())
print(EquivalenceClass() == 'MyClass')
