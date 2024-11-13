# Python3 code to demonstrate working of
# Filter rows with Extreme values greater than K
# Using filter() + lambda + min() + max()

# initializing list
test_list = [[3, 5, 1], [9, 1, 2], [3, 4, 2], [1, 10, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# max() and min() getting extreme difference
res = list(filter(lambda sub : max(sub) - min(sub) > K, test_list))

# printing result
print("Filtered rows : " + str(res))
