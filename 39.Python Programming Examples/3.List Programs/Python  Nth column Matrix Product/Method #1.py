# Python3 code to demonstrate working of
# Nth column Matrix Product
# using loop + zip()

def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initialize list
test_list = [[5, 6, 7],
			[9, 10, 2],
			[10, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 2

# Nth column Matrix Product
# using loop + zip()
res = [prod(idx) for idx in zip(*test_list)][N]

# printing result
print("Product of Nth column is : " + str(res))
