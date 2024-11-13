# Python3 code to demonstrate
# Sliced Product in List
# using list slicing + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [4, 5, 2, 6, 7, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 5

# Sliced Product in List
# using list slicing + loop
res = prod(test_list[:K])

# print result
print("The first K elements product of list is : " + str(res))
