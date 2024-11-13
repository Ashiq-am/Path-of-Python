# Python3 code to demonstrate working of
# Filter Tuples Product greater than K
# Using list comprehension

# getting product
def prod(box):
	res = 1
	for ele in box:
		res *= ele
	return res


# initializing list
test_list = [(4, 5, 7), (1, 2, 3), (8, 4, 2), (2, 3, 4)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 50

res = [sub for sub in test_list if prod(sub) > K]

# printing result
print("Tuples with product greater than K : " + str(res))
