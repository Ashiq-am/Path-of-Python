# Python3 code to demonstrate
# Sliced Product in List
# using islice() + loop
from itertools import islice

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
# using islice() + loop
res = list(islice(test_list, 0, K))
res = prod(res)

# print result
print("The first K elements product of list is : " + str(res))
