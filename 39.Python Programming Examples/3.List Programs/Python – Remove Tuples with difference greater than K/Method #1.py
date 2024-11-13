# Python3 code to demonstrate working of
# Remove Tuples with difference greater than K
# Using list comprehension

# initializing list
test_list = [(4, 8), (1, 7), (9, 12), (3, 12), (2, 10)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# filtering using list comprehension, checking for smaller than K diff.
res = [sub for sub in test_list if abs(sub[0] - sub[1]) <= K]

# printing result
print("Tuples List after removal : " + str(res))
