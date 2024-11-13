"""

"""


'''
For the enclosed scope, we need to define an outer function enclosing the inner function, 
comment out the local pi variable of inner function and refer to pi using the nonlocal keyword.
'''




# Enclosed Scope

pi = 'global pi variable'

def outer():
	pi = 'outer pi variable'
	def inner():
		# pi = 'inner pi variable'
		nonlocal pi
		print(pi)
	inner()

outer()
print(pi)
