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
