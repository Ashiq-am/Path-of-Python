# Python3 code to demonstrate working of
# Frequency of elements from other list
# Using dictionary comprehension + count()

# initializing lists
test_list1 = [4, 6, 8, 9, 10]
test_list2 = [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# count() used to perform count.
# returns 0 is no occurrence.
# ignores different new elements in list 2
res = {key : test_list2.count(key) for key in test_list1}

# printing result
print("Lists elements Frequency : " + str(res))
