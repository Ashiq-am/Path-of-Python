# Python code to demonstrate
# K Value Indices Product
# using naive method

# initializing list
test_list = [1, 3, 4, 3, 6, 7, 3]

# printing initial list
print ("Original list : " + str(test_list))

# initializing K
K = 3

# using naive method
# K Value Indices Product
res = 1
for i in range(0, len(test_list)) :
	if test_list[i] == K :
		res *= i

# printing resultant list
print ("K Value indices product is : " + str(res))
