# Python program to print the octal value of the
# numbers from 1 to N

# Function to find the octal value of the numbers
# in the range 1 to N
def octal_in_range(n):

	# For loop traversing from 1 to N (Both Inclusive)
	for i in range(1, n+1):

		# Printing octal value of i
		print(oct(i)[2:])


# Calling the function with input 3
print("Input: 3")
octal_in_range(3)

# Calling the function with input 11
print("Input: 11")
octal_in_range(11)
