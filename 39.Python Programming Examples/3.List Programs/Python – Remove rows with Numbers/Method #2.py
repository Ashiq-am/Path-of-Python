# Python3 code to demonstrate working of
# Remove rows with Numbers
# Using filter() + lambda + any()

# initializing lists
test_list = [[4, 'Gfg', 'best'], [
	'gfg', 'is', 'best'], [3, 5], ['GFG', 'Best']]

# printing original lists
print("The original list is : " + str(test_list))

# using isinstance to check for integer and not include them
# filter() used to filter with lambda fnc.
res = list(filter(lambda sub: not any(isinstance(ele, int)
									for ele in sub), test_list))

# printing result
print("The filtered rows : " + str(res))
