# Python3 code to demonstrate working of
# Dictionary Key's Product in list
# Using loop + itemgetter() + map()
import operator

def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# Initialize list
test_list = [{'gfg' : 1, 'is' : 2, 'best' : 3}, {'gfg' : 7, 'is' : 3, 'best' : 5}, {'gfg' : 9, 'is' : 8, 'best' : 6}]

# printing original list
print("The original list is : " + str(test_list))

# Dictionary Key's Product in list
# Using loop + itemgetter() + map()
res = prod(map(operator.itemgetter('gfg'), test_list))

# printing result
print("The product of particular key is : " + str(res))
