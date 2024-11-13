# Python3 code to demonstrate working of
# Sort Matrix by Maximum String Length
# Using sort() + len() + max()


def max_len(row):

	# getting Maximum length of string
	return max([len(ele) for ele in row])


# initializing list
test_list = [['gfg', 'best'], ['geeksforgeeks'],
			['cs', 'rocks'], ['gfg', 'cs']]

# printing original list
print("The original list is : " + str(test_list))

# performing sort()
test_list.sort(key=max_len)

# printing result
print("Sorted Matrix : " + str(test_list))
