# Python3 code to demonstrate working of
# Indices list of matching element from other list
# Using loop + count()

# initializing lists
test_list1 = [5, 7, 8, 9, 10, 11]
test_list2 = [8, 10, 11]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Indices list of matching element from other list
# Using loop + count()
res = []
i = 0
while (i < len(test_list1)):
	if (test_list2.count(test_list1[i]) > 0):
		res.append(i)
	i += 1

# printing result
print("The matching element Indices list : " + str(res))
