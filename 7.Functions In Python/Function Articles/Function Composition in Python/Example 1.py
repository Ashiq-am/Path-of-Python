# Function to add 2
# to a number
def add(x):
	return x + 2

# Function to multiply
# 2 to a number
def multiply(x):
	return x * 2

# Printing the result of
# composition of add and
# multiply to add 2 to a number
# and then multiply by 2
print("Adding 2 to 5 and multiplying the result with 2: ",
	multiply(add(5)))
