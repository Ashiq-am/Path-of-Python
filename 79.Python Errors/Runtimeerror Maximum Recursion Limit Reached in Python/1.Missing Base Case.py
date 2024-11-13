def endless_recursion(n):
	"""A recursive function without a proper base case"""
	return n * endless_recursion(n-1)

print(endless_recursion(5))
