# Python3 code to demonstrate
# Product of i ^ k in List
# using map() + loop + pow()

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

# initializing K
K = 4

# using map() + loop + pow()
# Product of i ^ k in List
res = prod(map(lambda i : pow(i, K), test_list))

# printing result
print ("The product of i ^ k of list is : " + str(res))
