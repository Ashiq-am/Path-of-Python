# Python3 code to demonstrate working of
# Dictionary Tuple Values Product
# Using tuple() + loop + zip() + values()

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# Initializing dictionary
test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3, 2), 'best' : (1, 4, 9)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Dictionary Tuple Values Product
# Using tuple() + loop + zip() + values()
res = tuple(prod(x) for x in zip(*test_dict.values()))

# printing result
print("The product from each index is : " + str(res))
