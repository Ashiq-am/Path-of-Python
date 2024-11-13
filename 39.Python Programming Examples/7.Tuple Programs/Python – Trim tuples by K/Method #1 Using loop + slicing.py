# Python3 code to demonstrate working of
# Trim tuples by K
# Using loop + slicing

# initializing list
test_list = [(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),
			(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

res = []
for ele in test_list:
	N = len(ele)

	# triming elements
	res.append(tuple(list(ele)[K: N - K]))

# printing result
print("Converted Tuples : " + str(res))
