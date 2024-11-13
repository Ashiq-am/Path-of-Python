# Python 3 code to demonstrate
# Unique values Multiplication
# using set() + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# Unique values Multiplication
# using set() + loop
res = prod(list(set(test_list)))

# Unique values Multiplication
# using set() + loop
# printing result
print ("The unique elements product : " + str(res))
