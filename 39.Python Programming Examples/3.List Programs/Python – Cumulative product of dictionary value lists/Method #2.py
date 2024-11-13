# Python3 code to demonstrate working of
# Cummulative product of dictionary value lists
# using loop + map()

def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initialize dictionary
test_dict = {'gfg' : [5, 6, 7], 'is' : [10, 11], 'best' : [19, 31, 22]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Cummulative product of dictionary value lists
# using loop + map()
res = sum(map(prod, test_dict.values()))

# printing result
print("Product of dictionary list values are : " + str(res))
