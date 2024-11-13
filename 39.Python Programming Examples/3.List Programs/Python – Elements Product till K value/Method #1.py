# Python 3 code to demonstrate
# Elements Product till K value
# using naive method

# initializing list
test_list = [1, 7, 5, 6, 3, 8]

# initializing k
k = 6

# printing list
print ("The list : " + str(test_list))

# using naive method
# Elements Product till K value
res = 1
for i in test_list :
	if i <= k :
		res *= i

# printing the product
print ("The product till K : " + str(res))
