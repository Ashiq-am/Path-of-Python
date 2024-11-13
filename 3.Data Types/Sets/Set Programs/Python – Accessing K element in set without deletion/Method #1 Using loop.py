# Python3 code to demonstrate working of
# Accessing K element in set without deletion
# Using loop

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing K
K = 7

res = -1
for ele in test_set:

	# checking for K element
	res += 1
	if ele == K:
		break

# printing result
print("Position of K in set : " + str(res))
