# Python program to find the
# factorial of a number

# Function name factorial is defined
def factorial(n):
	if n == 1:
		return n
	else:
		return n*factorial(n-1)

# Main code
num = 6

# check is the number is negative
if num < 0:
	print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
	print("The factorial of 0 is 1")
else:
	print("The factorial of", num, "is", factorial(num))
