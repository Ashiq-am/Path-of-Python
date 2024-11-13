# Python3 code to demonstrate
# Cubes Product in list
# using loop + max()

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [3, 5, 7, 9, 11]

# printing original list
print ("The original list is : " + str(test_list))

# using loop + max()
# Cubes Product in list
res = prod(map(lambda i : i * i * i, test_list))

# printing result
print ("The product of cubes of list is : " + str(res))
