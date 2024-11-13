# Python code to demonstrate
# K Value Indices Product
# using enumerate()

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [1, 3, 4, 3, 6, 7, 3]

# printing initial list
print ("Original list : " + str(test_list))

# initializing K
K = 3

# using enumerate()
# K Value Indices Product
res = prod([i for i, value in enumerate(test_list) if value == K])

# printing resultant list
print ("K Value indices product is : " + str(res))
