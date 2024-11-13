# Python3 code to demonstrate working of
# Filter Tuple with Elements capped on K
# Using all() + list comprehension

# initializing list
test_list = [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# using all() to check for each tuple being in K limit
res = [sub for sub in test_list if all(ele <= K for ele in sub)]

# printing result
print("The filtered tuples : " + str(res))
