# Python3 code to demonstrate working of
# Remove Similar Rows from Tuple Matrix
# Using set() + tuple() + sorted() + list comprehension

# initializing lists
test_list = [[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]]

# printing original list
print("The original list is : " + str(test_list))

# Remove Similar Rows from Tuple Matrix
# Using set() + tuple() + sorted() + list comprehension
res = set([tuple(set(sub)) for sub in test_list])

# printing result
print("Tuple matrix after removal : " + str(res))
