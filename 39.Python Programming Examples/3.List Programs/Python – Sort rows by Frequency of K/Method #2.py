# Python3 code to demonstrate working of
# Sort rows by Frequency of K
# Using sorted() + lambda + count()

# initializing list
test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1, 2, 2, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# performing inplace sort
res = sorted(test_list, key=lambda row: row.count(K))

# printing result
print("Sorted List : " + str(res))
