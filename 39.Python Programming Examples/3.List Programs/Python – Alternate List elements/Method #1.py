# Python3 code to demonstrate working of
# Alternate List elements
# Using loop

# initializing lists
test_list1 = [5, 3, 1, 4, 7]
test_list2 = [6, 4, 2, 5, 1]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Using loop to print elements in criss cross manner
res = []
for idx in range(0, len(test_list1)):
	res.append(test_list1[idx])
	res.append(test_list2[idx])

# printing result
print("The zig-zag printing of elements : " + str(res))
