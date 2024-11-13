# Python3 code to demonstrate working of
# Smallest missing element after K
# Using loop

# initializing list
test_list = [1, 3, 4, 5, 7, 9, 10]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 7

ele = 1

# infinite loop to break at element found
while(1):

		# checking if greater than K and not in list
	if ele > K and ele not in test_list:
		res = ele
		break
	ele = ele + 1

# printing result
print("The Smallest element greater than K in list : " + str(res))
