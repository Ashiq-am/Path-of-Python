# Function to combine two
# function which it accepts
# as argument
def composite_function(f, g):
	return lambda x : f(g(x))

# Function to add 2
def add(x):
	return x + 2

# Function to multiply 2
def multiply(x):
	return x * 2

# Composite function returns
# a lambda function. Here add_multiply
# will store lambda x : multiply(add(x))
add_multiply = composite_function(multiply, add)

print("Adding 2 to 5 and multiplying the result with 2: ",
	add_multiply(5))
