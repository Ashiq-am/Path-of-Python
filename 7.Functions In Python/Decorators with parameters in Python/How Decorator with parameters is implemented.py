
def decorators(*args, **kwargs):
	def inner(func):
		'''
		do operations with func
		'''
		return func
	return inner #this is the fun_obj mentioned in the above content

@decorators(params)
def func():
	"""
		function implementation
	"""





"""Here params can also be empty.
Above code can be visualized step by step here"""





# Python code to illustrate
# Decorators with parameters in Python

def decorator(*args, **kwargs):
	print("Inside decorator")
	def inner(func):
		print("Inside inner function")
		print("I like", kwargs['like'])
		return func
	return inner

@decorator(like = "geeksforgeeks")
def func():
	print("Inside actual function")

func()
