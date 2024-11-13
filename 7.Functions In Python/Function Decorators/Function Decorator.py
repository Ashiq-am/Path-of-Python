# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
def decorate_message(fun):

	# Nested function
	def addWelcome(site_name):
		return "Welcome to " + fun(site_name)

	# Decorator returns a function
	return addWelcome

@decorate_message
def site(site_name):
	return site_name;

# Driver code

# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeks"))




'''Decorators can also be useful to attach data (or add attribute) to functions.'''





# A Python example to demonstrate that
# decorators can be useful attach data

# A decorator function to attach
# data to func
def attach_data(func):
	func.data = 3
	return func

@attach_data
def add (x, y):
	return x + y

# Driver code

# This call is equivalent to attach_data()
# with add() as parameter
print(add(2, 3))

print(add.data)





"""‘add()’ returns sum of x and y passed as arguments but it is wrapped by a decorator function, 
calling add(2, 3) would simply give sum of two numbers but when we call add.data then ‘add’ function is passed 
into then decorator function ‘attach_data’ as argument and this function returns ‘add’ function with an attribute ‘data’ 
that is set to 3 and hence prints it.

Python decorators are a powerful tool to remove redundancy."""
