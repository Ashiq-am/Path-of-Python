# Python3 code to demonstrate working of
# Sort by Uppercase Frequency
# Using isupper() + sort()


# helper function
def upper_sort(sub):

	# len() to get total uppercase characters
	return len([ele for ele in sub if ele.isupper()])


# initializing list
test_list = ["Gfg", "is", "BEST", "FoR", "GEEKS"]

# printing original list
print("The original list is: " + str(test_list))

# using external function to perform sorting
test_list.sort(key=upper_sort)

# printing result
print("Elements after uppercase sorting: " + str(test_list))
