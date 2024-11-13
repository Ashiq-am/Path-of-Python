'''There’s another case of double leading and trailing underscores.
We follow this while using special variables or methods (called “magic method”) such as__len__, __init__.
These methods provide special syntactic features to the names. For example, __file__ indicates the location of
Python file, __eq__ is executed when a == b expression is executed.
Example:'''



# Python code to illustrate double leading and
# double trailing underscore works
class Geek:

	# '__init__' for initializing, this is a
	# special method
	def __init__(self, ab):
		self.ab = ab

	# custom special method. try not to use it
	def __custom__(self):
		pass
