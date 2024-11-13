# Python3 code to demonstrate
# K Summation from Two lists
# using loop

# Initializing lists
test_list1 = [3, 2, 5]
test_list2 = [4, 3, 6, 8, 7]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Initializing K
K = 9

# K Summation from Two lists
# using loop
res = []
for idx in test_list1:
	val_req = K - idx
	for j in test_list2:
		if j == val_req:
			x, y = j, idx
			res.append((x, y))

# printing result
print ("Summation pairs among lists : " + str(res))
