# Python3 code to demonstrate working of
# Filter Tuples with Integers
# Using all() + list comprehension + isinstance()

# initializing list
test_list = [(4, 5, "GFg"), (5, 6), (3,), ("Gfg",)]

# printing original list
print("The original list is : " + str(test_list))

# list comprehension to encapsulate in 1 liner
res = [sub for sub in test_list if all(isinstance(ele, int) for ele in sub)]

# printing results
print("Filtered tuples : " + str(res))
