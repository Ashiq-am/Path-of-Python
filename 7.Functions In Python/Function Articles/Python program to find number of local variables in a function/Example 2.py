# Python program to find number of
# local variables in a function

# A function containing no variables
def geek():
	pass

# A function containing 3 variables
def fun():
	a, b, c = 1, 2.25, 333
	str = 'GeeksForGeeks'

# Driver program
print(geek.__code__.co_nlocals)
print(fun.__code__.co_nlocals)
