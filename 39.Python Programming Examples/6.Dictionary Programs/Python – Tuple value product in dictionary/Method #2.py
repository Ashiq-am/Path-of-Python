# Python3 code to demonstrate working of
# Dictionary Tuple Values Product
# Using tuple() + map() + values()

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
# Using tuple() + map() + values()
temp = []
for sub in test_dict.values():
	temp.append(list(sub))
res = tuple(map(prod, temp))

# printing result
print("The product from each index is : " + str(res))
