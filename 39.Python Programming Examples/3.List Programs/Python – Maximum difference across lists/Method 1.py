# Python3 code to demonstrate working of
# Maximum difference across lists
# Using list comprehension + max()

# initializing lists
test_list1 = [3, 4, 2, 1, 7]
test_list2 = [6, 2, 1, 9, 1]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using max() to get maximum of extracted difference
res = max(abs(test_list2[idx] - test_list1[idx])
		for idx in range(0, len(test_list1) - 1))

# printing result
print("Maximum difference among lists : " + str(res))
