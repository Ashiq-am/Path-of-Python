# Python3 code to demonstrate working of
# Filter Tuples with All Even Elements
# Using all() + list comprehension

# initializing list
test_list = [(6, 4, 2, 8), (5, 6, 7, 6), (8, 0, 2), (7, )]

# printing original list
print("The original list is : " + str(test_list))

# testing for tuple to be even using all()
res = [sub for sub in test_list if all(ele % 2 == 0 for ele in sub)]

# printing results
print("Filtered Tuples : " + str(res))
