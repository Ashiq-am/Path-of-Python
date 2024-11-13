# Python3 code to demonstrate working of
# Random range in list
# Using randrange() + slicing
import random


# function to Random range in list
def rabdomRangeList(test_list):
	# getting ranges
	strt_idx = random.randrange(0, len(test_list) - 1)
	end_idx = random.randrange(strt_idx, len(test_list) - 1)

	# getting range elements
	res = test_list[strt_idx: end_idx]

	return str(res)


# Driver Code
# initializing list
input_list1 = [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]

# printing original list
print("\nThe original list is : ", input_list1)

# printing result
print("Required List : " + rabdomRangeList(input_list1))


# initializing list
input_list2 = [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]

# printing original list
print("\nThe original list is : ", input_list2)

# printing result
print("Required List : " + rabdomRangeList(input_list2))


# initializing list
input_list3 = [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]

# printing original list
print("\nThe original list is : ", input_list3)

# printing result
print("Required List : " + rabdomRangeList(input_list3))
