# func will be func = type(func) -> <class 'function'>
@type
def func():
	return 42

print(func)

# print doesn't return anything, so func == None
@print
def func2():
	return 42

# Prints None
print(func2)
