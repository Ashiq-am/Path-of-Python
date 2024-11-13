# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj




#The destructor was called after the program ended or when all the references to object are deleted
#i.e when the reference count becomes zero, not when object went out of scope.