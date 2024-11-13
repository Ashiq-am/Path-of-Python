# Python3 code to demonstrate
# Zip Uneven Tuple
# using enumerate() + loop

# initializing tuples
test_tup1 = (7, 8, 4, 5, 9, 10)
test_tup2 = (1, 5, 6)

# printing original tuples
print ("The original tuple 1 is : " + str(test_tup1))
print ("The original tuple 2 is : " + str(test_tup2))

# using enumerate() + loop
# Zip Uneven Tuple
res = []
for i, j in enumerate(test_tup1):
	res.append((j, test_tup2[i % len(test_tup2)]))

# printing result
print ("The zipped tuple is : " + str(res))
