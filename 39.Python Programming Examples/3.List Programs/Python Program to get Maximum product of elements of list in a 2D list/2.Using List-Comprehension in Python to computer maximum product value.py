# function to calculate product
# of a list of elements

def prod(ll):
	z = 1
	for i in ll:
		z *= i
	return z

# driver code
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max_prod = max([prod(inner_list) for inner_list in l])
print(max_prod)
