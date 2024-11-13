# Python3 code to demonstrate working of
# Average digit greater than K
# Using sum() + len() + filter() + lambda

# initializing list
test_list = [633, 719, 8382, 119, 327]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# getting average and checking if greater than K
# using filter() and lambda to filter
res = list(filter(lambda sub: sum(
	[int(ele) for ele in str(sub)]) / len(str(sub)) >= K, test_list))

# printing result
print("Filtered List : " + str(res))
