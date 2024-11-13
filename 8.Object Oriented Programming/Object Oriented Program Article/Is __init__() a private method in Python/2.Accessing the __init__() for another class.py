# initialising class
class Demo:

	# defining a constructor
	def __init__(self):
		print("Init for base class")


class child(Demo):

	def __init__(self):
		Demo.__init__(self)
		print("Init for the child class")


# Driver code
obj1 = Demo()
obj2 = child()
