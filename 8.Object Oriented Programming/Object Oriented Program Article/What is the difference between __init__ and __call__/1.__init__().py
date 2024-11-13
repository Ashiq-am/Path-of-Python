class A:
	def __init__(self, x):
		print("inside __init__()")
		self.y = x

	def __str__(self):
		print("inside __str__()")
		print("value of y:", str(self.y))

# declaration of instance of class A
a = A(3)

# calling __str__() for object a
a.__str__()

# declaration of another instance
# of class A
b = A(10)

# calling __str__() for b
b.__str__()
