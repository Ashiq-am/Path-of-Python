def factorial(n):
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers")
	if n == 0:
		return 1
	result = 1
	try:
		for i in range(1, n + 1):
			result *= i
	except OverflowError:
		raise OverflowError("Factorial calculation resulted in overflow")
	return result

# Example usage of custom factorial function
try:
	print(factorial(10000))
except OverflowError as e:
	print("Overflow Error:", e)
