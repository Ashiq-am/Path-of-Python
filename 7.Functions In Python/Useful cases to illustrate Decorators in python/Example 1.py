# Python program to demonstrate
# decorators


# Creating a decorator
def decorated_func(func):
	def inner():
		print("This is decorated function")
		func()
	return inner()


def ordinary_func ():
	print("This is ordinary function")

decorated = decorated_func(ordinary_func)
decorated
