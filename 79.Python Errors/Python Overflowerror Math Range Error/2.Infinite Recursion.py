def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

# Calling the factorial function with a large number
result = factorial(10000)
print(result)
