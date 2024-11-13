# Python3 code to demonstrate working of
# Record Index Product
# using zip() + map() + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initialize list
test_list = [(1, 2, 3), (6, 7, 6), (1, 6, 8)]

# printing original list
print("The original list : " + str(test_list))

# Record Index Product
# using zip() + map() + loop
res = list(map(prod, zip(*test_list)))

# printing result
print("The Cummulative column product is : " + str(res))
