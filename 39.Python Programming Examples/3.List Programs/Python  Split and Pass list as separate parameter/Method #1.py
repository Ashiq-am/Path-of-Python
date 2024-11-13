# Python3 code to demonstrate working of
# Split and Pass list as separate parameter
# using tuple()

# Helper function for demonstration
def pass_args(arg1, arg2):
	print("The first argument is : " + str(arg1))
	print("The second argument is : " + str(arg2))

# initialize list
test_list = [4, 5]

# printing original list
print("The original list is : " + str(test_list))

# Split and Pass list as separate parameter
# using tuple()
one, two = tuple(test_list)
pass_args(one, two)
