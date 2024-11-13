# Python3 code to demonstrate working of
# Extract Even elements in Nested Mixed Tuple
# Using recursion + isinstance() + loop

# helper_fnc
def even_ele(test_tuple, even_fnc):
	res = tuple()
	for ele in test_tuple:
		if isinstance(ele, tuple):
			res += (even_ele(ele, even_fnc), )
		elif even_fnc(ele):
			res += (ele, )
	return res

# initializing tuples
test_tuple = (4, 5, (7, 6, (2, 4)), 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Extract Even elements in Nested Mixed Tuple
# Using recursion + isinstance() + loop
res = even_ele(test_tuple, lambda x: x % 2 == 0)

# printing result
print("Even elements of tuple : " + str(res))
