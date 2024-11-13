# Python3 code to demonstrate working of
# Index match element Product
# using loop + zip()

def prod(val) :
	res = 1
	for ele in list(val):
		res *= ele
	return res

# initialize lists
test_list1 = [5, 6, 10, 4, 7, 1, 19]
test_list2 = [6, 6, 10, 3, 7, 10, 19]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Index match element Product
# using loop + zip()
res = prod(x for x, y in zip(test_list1, test_list2) if x == y)

# printing result
print("Multiplication of Identical elements : " + str(res))
