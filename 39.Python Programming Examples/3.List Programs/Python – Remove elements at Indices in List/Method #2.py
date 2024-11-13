# Python3 code to demonstrate working of
# Remove elements at Indices in List
# Using enumerate() + list comprehension

# initializing list
test_list = [5, 6, 3, 7, 8, 1, 2, 10]

# printing original list
print("The original list is : " + str(test_list))

# initializing idx list
idx_list = [2, 4, 5, 7]

# one-liner to test for element in index list
res = [ele for idx, ele in enumerate(test_list) if idx not in idx_list]

# printing results
print("Filtered List after removal : " + str(res))
