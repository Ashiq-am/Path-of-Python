class MyEquivalence(object):
	def __eq__(self, other):
		print('MyEquivalence:\n'
			'% r\n % r' %(self, other))
		return self is other

class YourEquivalence(object):
	def __eq__(self, other):
		print('Your Equivalence:\n'
			'% r\n % r' %(self, other))
		return self is other

eq1 = MyEquivalence()
eq2 = YourEquivalence()
# checking for equivalence where eq1 is at the left side
print(eq1 == eq2)
# checking for equivalence where eq2 is at the left side
print(eq2 == eq1)
