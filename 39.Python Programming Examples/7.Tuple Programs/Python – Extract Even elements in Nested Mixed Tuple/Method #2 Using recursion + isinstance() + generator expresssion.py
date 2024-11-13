# Python3 code to demonstrate working of
# Extract Even elements in Nested Mixed Tuple
# Using recursion + isinstance() + generator expresssion

# helper_fnc
def even_ele(test_tuple, even_fnc):
	return tuple(even_ele(ele, even_fnc) if isinstance(ele, tuple) else ele
	for ele in test_tuple if isinstance(ele, tuple) or even_fnc(ele))

# initializing tuples
test_tuple = (4, 5, (7, 6, (2, 4)), 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Extract Even elements in Nested Mixed Tuple
# Using recursion + isinstance() + generator expresssion
res = even_ele(test_tuple, lambda x: x % 2 == 0)

# printing result
print("Even elements of tuple : " + str(res))
