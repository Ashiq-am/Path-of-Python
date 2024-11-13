# Python3 code to demonstrate
# Product of Squares in List
# using sum() + max()

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

# using sum() + max()
# Product of Squares in List
res = prod(map(lambda i : i * i, test_list))

# printing result
print ("The product of squares of list is : " + str(res))
