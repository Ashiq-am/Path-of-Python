# Python3 code to demonstrate
# Column Product in List of lists
# using map() + loop + zip()

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]

# printing original list
print("The original list : " + str(test_list))

# using map() + loop + zip()
# Column Product in List of lists
res = list(map(prod, zip(*test_list)))

# print result
print("The Product of each index list is : " + str(res))
