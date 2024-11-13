# Python3 code to demonstrate working of
# Average digit greater than K
# Using sum() + len() + list comprehension

# initializing list
test_list = [633, 719, 8382, 119, 327]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# getting average and checking if greater than K
res = [sub for sub in test_list if sum(
	[int(ele) for ele in str(sub)]) / len(str(sub)) >= K]

# printing result
print("Filtered List : " + str(res))
