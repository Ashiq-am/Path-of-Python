class MyEquivalence(object):
	def __eq__(self, other):
		print('MyEquivalence:\n'
			'% r\n % r' %(self, other))
		return self is other

class MySubEquivalence(MyEquivalence):
	def __eq__(self, other):
		print('MySubEquivalence:\n'
			'% r\n % r' %(self, other))
		return self is other

eqMain = MyEquivalence()
eqSub = MySubEquivalence()

# eqMain at the right side
print(eqMain == eqSub)

# eqSub at the right side
print(eqSub == eqMain)
