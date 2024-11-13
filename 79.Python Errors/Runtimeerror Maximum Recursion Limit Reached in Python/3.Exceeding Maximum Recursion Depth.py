def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# Testing the factorial function
result = factorial(1001)
print(result)
