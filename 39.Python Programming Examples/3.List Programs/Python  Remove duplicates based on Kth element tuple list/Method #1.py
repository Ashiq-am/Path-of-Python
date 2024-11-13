# Python3 code to demonstrate working of
# Remove duplicates based on Kth element tuple list
# Using loop

# initialize list
test_list = [(3, 1, 5), (1, 3, 6), (2, 1, 7),
						(5, 2, 8), (6, 3, 0)]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 1

# Remove duplicates based on Kth element tuple list
# Using loop
temp = set()
res = []
for ele in test_list:
	if ele[K] not in temp:
		res.append(ele)
		temp.add(ele[K])

# printing result
print("The list after removal of K based duplicates : " + str(res))
