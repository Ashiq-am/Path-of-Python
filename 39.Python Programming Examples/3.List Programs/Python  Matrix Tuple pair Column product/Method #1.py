# Python3 code to demonstrate
# Matrix Tuple pair Column product
# using list comprehension + zip()

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [[(1, 4), (2, 3), (5, 2)], [(3, 7), (1, 9), (10, 5)]]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + zip()
# Matrix Tuple pair Column product
res = [tuple(prod(j) for j in zip(*i)) for i in zip(*test_list)]

# print result
print("The product of columns of tuple list : " + str(res))
