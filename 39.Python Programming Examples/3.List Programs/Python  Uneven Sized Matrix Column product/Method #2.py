# Python3 code to demonstrate
# Uneven Sized Matrix Column product
# using list comprehension + loop + zip_longest()
import itertools

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

# using list comprehension + loop + zip_longest()
# Uneven Sized Matrix Column product
res = [prod(i) for i in itertools.zip_longest(*test_list, fillvalue = 1)]

# printing result
print ("The product of columns is : " + str(res))
