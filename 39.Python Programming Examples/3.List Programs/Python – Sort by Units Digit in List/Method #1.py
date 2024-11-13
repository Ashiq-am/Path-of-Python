# Python3 code to demonstrate working of
# Sort by Units Digit in List
# Using sort() + str()

# helpr_fnc to sort


def unit_sort(ele):

	# get last element
	return str(ele)[-1]


# initializing lists
test_list = [76, 434, 23, 22342]

# printing original lists
print("The original list is : " + str(test_list))

# inplace sort by unit digits
test_list.sort(key=unit_sort)

# printing result
print("The unit sorted list : " + str(test_list))
