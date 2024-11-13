
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
