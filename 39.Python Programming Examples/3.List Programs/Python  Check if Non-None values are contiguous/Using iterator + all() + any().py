# Python3 code to demonstrate working of
# Check if Non-None values are contiguous
# Using iterator + all() + any()

# helper function
def check_cont(test_list):
	test_list = iter(test_list)
	all(x is None for x in test_list)
	any(x is None for x in test_list)
	return all(x is None for x in test_list)

# initializing list
test_list = [None, None, 'Gfg', 'is', 'Good', None, None, None]

# printing list
print("The original list : " + str(test_list))

# Check if Non-None values are contiguous
# Using iterator + all() + any()
res = check_cont(test_list)

# Printing result
print("Are non-none values contiguous ? : " + str(res))
