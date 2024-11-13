# Python3 code to demonstrate working of
# Extract tuples with elements in Range
# Using all() + list comprehension

# initializing list
test_list = [(4, 5, 7), (5, 6), (3, 8, 10), (4, 10)]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
strt, end = 4, 7

# list comprehension to encapsulate in 1 liner
# all() checks for all elements in range
res = [sub for sub in test_list if all(ele >= strt and ele <= end for ele in sub)]

# printing results
print("Filtered tuples : " + str(res))
