# Python3 code to demonstrate working of
# Group consecutive list elements with tolerance
# Using generator

# helper generator
def split_tol(test_list, tol):
	res = []
	last = test_list[0]
	for ele in test_list:
		if ele-last > tol:
			yield res
			res = []
		res.append(ele)
		last = ele
	yield res

# initializing list
test_list = [1, 2, 4, 5, 9, 11, 13, 24, 25, 26, 28]

# printing original list
print("The original list is : " + str(test_list))

# Group consecutive list elements with tolerance
# Using generator
res = list(split_tol(test_list, 2))

# printing result
print("The splitted list is : " + str(res))
