"""Two underlines, in the beginning, cause a lot of confusion.
This is about syntax rather than a convention. double underscore will mangle the attribute names of a
class to avoid conflicts of attribute names between classes.


For example:"""




# Python code to illustrate how double
# underscore at the beginning works
class Geek:
	def _single_method(self):
		pass
	def __double_method(self): # for mangling
		pass
class Pyth(Geek):
	def __double_method(self): # for mangling
		pass
