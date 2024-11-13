# Python3 code to demonstrate
# Nested List Intersection Matrix Product
# using map() + intersection() + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list of lists
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# printing original list
print ("The original list is : " + str(test_list))

# Common Row elements Summation
# using map() + intersection() + loop
res = prod(list(set.intersection(*map(set, test_list))))

# printing result
print ("The common row elements product is : " + str(res))
