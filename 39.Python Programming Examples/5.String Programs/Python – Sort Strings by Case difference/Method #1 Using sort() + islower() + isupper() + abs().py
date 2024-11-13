# Python3 code to demonstrate working of
# Sort Strings by Case difference
# Using sort() + islower() + isupper() + abs()


def get_case_diff(string):

	# getting case count and difference
	lower_cnt = len([ele for ele in string if ele.islower()])
	upper_cnt = len([ele for ele in string if ele.isupper()])
	return abs(lower_cnt - upper_cnt)


# initializing Matrix
test_list = ["GFG", "GeeKs", "best", "FOr", "alL", "GEEKS"]

# printing original list
print("The original list is : " + str(test_list))

# inplace sort using sort()
test_list.sort(key=get_case_diff)

# printing result
print("Sorted Strings by case difference : " + str(test_list))
