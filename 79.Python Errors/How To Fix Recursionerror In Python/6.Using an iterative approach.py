# Function to calculate the factorial of a number using an iterative approach
def factorial_iterative(n):
	# Initialize the result to 1
	result = 1

	# Iterate from 1 to n (inclusive)
	for i in range(1, n + 1):
		# Multiply the current result by the current value of i
		result *= i

	# Return the final result after the loop
	return result

#Examples

result = factorial_iterative(1001)

print(result)
