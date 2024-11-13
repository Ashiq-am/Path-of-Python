# Python3 code to demonstrate
# Test Common Elements Order
# using loop + set()

# helper function
def common_ord(test_list1, test_list2):
	comm = set(test_list1)
	comm.intersection_update(test_list2)
	pr_idx = 0
	for ele in test_list1:
		if ele in comm:
			try:
				pr_idx = test_list2.index(ele, pr_idx)
			except ValueError:
				return False
	return True

# Initializing lists
test_list1 = ['Gfg', 'is', 'for', 'Geeks']
test_list2 = [1, 'Gfg', 2, 'Geeks']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Test Common Elements Order
# using loop + set()
res = common_ord(test_list1, test_list2)

# printing result
print ("Are common elements in order ? : " + str(res))
