# Python3 code to demonstrate working of
# Maximum difference across lists
# Using zip() + max()

# initializing lists
test_list1 = [3, 4, 2, 1, 7]
test_list2 = [6, 2, 1, 9, 1]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using max() to get maximum of extracted difference
# zip() used to bind elements
res = max(abs(ele1 - ele2) for ele1, ele2 in zip(test_list1, test_list2))

# printing result
print("Maximum difference among lists : " + str(res))
