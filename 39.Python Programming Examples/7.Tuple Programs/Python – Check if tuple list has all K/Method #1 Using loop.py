# Python3 code to demonstrate working of
# Check if tuple list has all K
# Using loop

# initializing list
test_list = [(4, 4), (4, 4, 4), (4, 4), (4, 4, 4, 4), (4, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# Check if tuple list has all K
# Using loop
res = True
for tup in test_list:
	for ele in tup:
		if ele != K:
			res = False

# printing result
print("Are all elements K ? : " + str(res))
