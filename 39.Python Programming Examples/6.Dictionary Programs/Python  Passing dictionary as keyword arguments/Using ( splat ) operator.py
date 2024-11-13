# Python3 code to demonstrate working of
# Passing dictionary as keyword arguments
# Using ** ( splat ) operator

# Helper function to demo this task
def test_func(a = 4, b = 5):
	print("The value of a is : " + str(a))
	print("The value of b is : " + str(b))

# initializing dictionary
test_dict = {'a' : 1, 'b' : 2}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Testing with default values
print("The default function call yields : ")
test_func()

print("\r")

# Passing dictionary as keyword arguments
# Using ** ( splat ) operator
print("The function values with splat operator unpacking : ")
test_func(**test_dict)
