import sys

def num_sort(strn):

	# getting number using isdigit() and split()
	computed_num = [ele for ele in strn.split() if ele.isdigit()]

	# assigning lowest weightage to strings
	# with no numbers
	if len(computed_num) > 0:
		return int(computed_num[0])
	return -1


# initializing Matrix
test_list = ["gfg is", "all no 7", "geeks over seas", "and planets 5"]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
test_list.sort(key=num_sort)

# printing result
print("Sorted Strings : " + str(test_list))
