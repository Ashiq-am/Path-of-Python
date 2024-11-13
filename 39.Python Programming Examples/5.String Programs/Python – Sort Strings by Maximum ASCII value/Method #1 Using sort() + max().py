# Python3 code to demonstrate working of
# Sort Strings by Maximum Character
# Using sort() + max()

# get maximum character fnc.
def get_max(sub):

	# returns maximum character
	return ord(max(sub))


# initializing list
test_list = ["geeksforgeeks", "is", "best", "for", "cs"]

# printing original lists
print("The original list is : " + str(test_list))

# performing sorting
test_list.sort(key=get_max)

# printing result
print("Sorted List : " + str(test_list))
