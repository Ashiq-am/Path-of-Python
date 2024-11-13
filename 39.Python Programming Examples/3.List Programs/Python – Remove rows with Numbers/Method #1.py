# Python3 code to demonstrate working of
# Remove rows with Numbers
# Using list comprehension + any

# initializing lists
test_list = [[4, 'Gfg', 'best'], [
	'gfg', 'is', 'best'], [3, 5], ['GFG', 'Best']]

# printing original lists
print("The original list is : " + str(test_list))

# using isinstance to check for integer and not include them
res = [sub for sub in test_list if not any(
	isinstance(ele, int) for ele in sub)]

# printing result
print("The filtered rows : " + str(res))
