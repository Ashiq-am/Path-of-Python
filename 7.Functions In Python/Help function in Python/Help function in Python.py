help(print)


"""It gives the following output: 


Help function output can also be defined for user defined functions and classes. 
The docstring(documentation string) is used for documentation. 

It is nested inside triple quotes and is the first statement within a class or function or a module."""








"""Let us define a class with functions:"""


class Helper:
	def __init__(self):
		'''The helper class is initialized'''

	def print_help(self):
		'''Returns the help description'''
		print('helper description')

help(Helper)
help(Helper.print_help)
