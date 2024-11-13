# Python3 code to demonstrate working of
# Convert Matrix to Sets of Set
# Using map() + frozenset() + set()

# initializing list
test_list = [[5, 6, 3], [1, 7, 9], [8, 2, 0]]

# printing original list
print("The original list is : " + str(test_list))

# map() to extend logic to inner elements
res = set(map(frozenset, test_list))

# printing result
print("Converted set Matrix : " + str(res))
