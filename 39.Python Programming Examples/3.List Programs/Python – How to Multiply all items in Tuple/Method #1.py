# Python3 code to demonstrate working of
# Tuple Elements Multiplication
# Using list() + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing tup
test_tup = (7, 8, 9, 1, 10, 7)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Tuple Elements Multiplication
# Using list() + loop
res = prod(list(test_tup))

# printing result
print("The product of tuple elements are : " + str(res))
