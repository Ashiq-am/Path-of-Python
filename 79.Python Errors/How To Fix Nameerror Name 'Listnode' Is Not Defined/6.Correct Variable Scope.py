# Correct: Correct variable scope
class Listnode:
	pass

def some_function():
	node = Listnode() # Correct scope

some_function() # No NameError now
