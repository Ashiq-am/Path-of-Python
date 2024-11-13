# Python3 code to demonstrate working of
# Count of matching elements among lists [ Including duplicates ]
# Using loop

# initializing lists
test_list1 = [3, 5, 6, 7, 2, 3]
test_list2 = [5, 5, 3, 9, 8]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using loop to iterate each element
res = 0
for ele in test_list1:
	if ele in test_list2:
		res += 1

# printing result
print("All matching elements : " + str(res))
