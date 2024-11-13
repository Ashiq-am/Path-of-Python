# Python3 code to demonstrate working of
# Custom Pool Sorting
# Using sort() + comparator key function

# comparator function
def func(ele):

	# Returning 1 or 2 ro assign priority
	if ele in prio1_list:
		return 1
	elif ele in prio2_list:
		return 2

# initializing list
test_list = [5, 6, 3, 7, 4, 2, 9, 10]

# printing original list
print("The original list is : " + str(test_list))

# initializing priority lists
prio1_list = [4, 6, 3, 8, 10]
prio2_list = [5, 7, 1, 2, 9]

# Using sort() + comparator key function
# key passed with function to manage priority
test_list.sort(key = func)

# printing result
print("List after sorting : " + str(test_list))
