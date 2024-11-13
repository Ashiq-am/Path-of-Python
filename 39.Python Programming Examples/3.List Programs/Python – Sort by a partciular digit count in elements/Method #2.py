# Python3 code to demonstrate working of
# Sort by digit count in elements
# Using sorted() + str() + count() + lambda

# initializing list
test_list = [4322, 2122, 123, 1344]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# sorting using sorted()
# not inplace sort.
res = sorted(test_list, key = lambda ele : str(ele).count(str(K)))

# printing result
print("Sorted list : " + str(res))
