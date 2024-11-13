# Python3 code to demonstrate working of
# Convert Matrix to Sets of Set
# Using set() + frozenset() + generator expression

# initializing list
test_list = [[5, 6, 3], [1, 7, 9], [8, 2, 0]]

# printing original list
print("The original list is : " + str(test_list))

# frozenset() to get inner elements hashable required for set()
res = set(frozenset(sub) for sub in test_list)

# printing result
print("Converted set Matrix : " + str(res))
