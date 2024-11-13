# Python code to demonstrate
# Uneven Sized Matrix Column product
# using loop + filter() + map() + list comprehension

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list of lists
test_list = [[1, 5, 3], [4], [9, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# using loop + filter() + map() + list comprehension
# Uneven Sized Matrix Column product
res = [prod(filter(None, j)) for j in map(None, *test_list)]

# printing result
print ("The product of columns is : " + str(res))
