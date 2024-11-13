# Python3 code to demonstrate working of
# Extract Even indexed elements in Tuple
# Using recursion

def helper_fnc(test_tuple):
	if len(test_tuple) == 0 or len(test_tuple) == 1:
		return ()
	return (test_tuple[0], ) + helper_fnc(test_tuple[2:])

# initializing tuples
test_tuple = (5, 'Gfg', 2, 8.8, 1.2, 'is')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Extract Even indexed elements in Tuple
# Using recursion
res = helper_fnc(test_tuple)

# printing result
print("The even indexed elements : " + str(res))
