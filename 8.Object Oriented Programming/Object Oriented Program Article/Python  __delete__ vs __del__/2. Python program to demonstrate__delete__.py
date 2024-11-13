# Python program to demonstrate
# __delete__


class Example(object):

	# Initializing
	def __init__(self):
		print("Example Instance.")

	# Calling __delete__
	def __delete__(self, instance):
		print ("Deleted in Example object.")


# Creating object of Example
# class as an descriptor attribute
# of this class
class Foo(object):
	exp = Example()

# Driver's code
f = Foo()
del f.exp
