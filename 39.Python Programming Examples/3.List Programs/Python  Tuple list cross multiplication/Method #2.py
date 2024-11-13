# Python3 code to demonstrate working of
# Tuple list cross multiplication
# using max() + zip() + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initialize lists
test_list1 = [(2, 4), (6, 7), (5, 1)]
test_list2 = [(5, 4), (8, 10), (8, 14)]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Tuple list cross multiplication
# using max() + zip() + loop
res = [tuple(map(prod, zip(a, b))) for a, b in zip(test_list1, test_list2)]

# printing result
print("The multiplication across lists is : " + str(res))
