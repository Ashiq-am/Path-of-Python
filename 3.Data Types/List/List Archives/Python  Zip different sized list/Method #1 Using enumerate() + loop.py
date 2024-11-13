# Python3 code to demonstrate
# zipping of two different size list
# using enumerate() + loop

# initializing lists
test_list1 = [7, 8, 4, 5, 9, 10]
test_list2 = [1, 5, 6]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using enumerate() + loop
# zipping of two different size list
res = []
for i, j in enumerate(test_list1):
	res.append((j, test_list2[i % len(test_list2)]))

# printing result
print ("The zipped list is : " + str(res))
