# Python3 code to demonstrate working of
# Replace Non-Maximum Records
# Using loop + map() + filter() + lambda

# initializing list
test_list = [(1, 4), (9, 11), (4, 6), (6, 8), (9, 11)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = None

# Replace Non-Maximum Records
# Using loop + map() + filter() + lambda
res = []
temp = list(filter(lambda ele: ele == max(test_list), test_list))
for ele in test_list:
	if ele not in temp:
		res.append(K)
	else :
		res.append(ele)

# printing result
print("The list after replacing Non-Maximum : " + str(res))
