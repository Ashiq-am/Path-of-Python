# Python 3 code to demonstrate
# Maximum element till K value
# using naive method

# initializing list
test_list = [1, 7, 5, 6, 3, 8]

# initializing k
k = 4

# printing list
print ("The list : " + str(test_list))

# using naive method
# Maximum element till K value
res = 0
for i in test_list :
	if i <= k :
		res = max(res, i)

# printing the intersection
print ("The maximum number till K : " + str(res))
