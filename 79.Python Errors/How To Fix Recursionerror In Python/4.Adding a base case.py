def factorial_recursive_with_base_case(n):
	# Base case: when n is 0, return 1
	if n == 0:
		return 1

	# Recursive call
	return n * factorial_recursive_with_base_case(n - 1)

if __name__ == '__main__':
	# Example: calculating the factorial of 100
	result = factorial_recursive_with_base_case(100)
	print(result)
