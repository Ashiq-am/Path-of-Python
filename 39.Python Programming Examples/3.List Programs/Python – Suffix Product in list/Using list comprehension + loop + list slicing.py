# Python3 code to demonstrate
# Suffix List Product
# using list comprehension + loop + list slicing

# compute prod
def prod(test_list):
	res = 1
	for ele in test_list:
		res = res * ele
	return res

# initializing list
test_list = [3, 4, 1, 7, 9, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + loop + list slicing
# Suffix List Product
test_list.reverse()
res = [prod(test_list[ : i + 1 ]) for i in range(len(test_list))]

# print result
print("The suffix product list is : " + str(res))
