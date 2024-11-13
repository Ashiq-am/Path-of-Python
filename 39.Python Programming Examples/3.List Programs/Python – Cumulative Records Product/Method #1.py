# Python3 code to demonstrate working of
# Cummulative Records Product
# using loop + generator expression

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# printing original list
print("The original list : " + str(test_list))

# Cummulative Records Product
# using loop + generator expression
res = prod(int(j) for i in test_list for j in i)

# printing result
print("The Cummulative product of list is : " + str(res))
