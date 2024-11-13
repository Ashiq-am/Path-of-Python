# Python3 code to demonstrate
# Modulo K elements removal
# using naive method

# initializing list
test_list = [1, 9, 4, 7, 6, 5, 8, 3]

# printing original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using naive method
# Modulo K elements removal
res = []
for val in test_list:
	if (val % K) :
		res.append(val)

# printing result
print ("List after removal of modulo K values : " + str(res))
