# Python program to illustrate the use of args which
# multiplies all the values given to the function as parameter

def multiplyAll(*values):
	mul = 1

	# values(args) will be in the form of tuple
	print(values)
	print("Type = ", type(values))


	# Multiplying the all the parameters and return the result
	for i in values:
		mul = mul * i

	return mul


# Driver program to test above function

# Multiply two numbers using above function
ans = multiplyAll(1,2)
print("The multiplication of 1 and 2 is ", ans)

# Multiply 5 numbers using above function
ans = multiplyAll(3, 4, 5, 6, 7)
print("The multiplication of 3 to 7 is ", ans)













"""Note that args are denoted by using a single star and kwargs are denoted by two stars before the 
formal parameters in the function."""
