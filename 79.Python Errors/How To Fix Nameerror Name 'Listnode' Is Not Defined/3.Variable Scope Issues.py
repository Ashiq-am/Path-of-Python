# Incorrect: Incorrect variable scope
def some_function():
	node = Listnode() # Incorrect scope

some_function() # Raises NameError
