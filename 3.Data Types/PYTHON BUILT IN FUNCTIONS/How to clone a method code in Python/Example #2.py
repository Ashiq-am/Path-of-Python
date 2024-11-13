def multiply(a, b):
	return a * b

# Using methodName.__code__.replace(co_posonlyargcount = 1) method
multiply.__code__ = multiply.__code__.replace(co_posonlyargcount = 2)

print(multiply(5, 6))
