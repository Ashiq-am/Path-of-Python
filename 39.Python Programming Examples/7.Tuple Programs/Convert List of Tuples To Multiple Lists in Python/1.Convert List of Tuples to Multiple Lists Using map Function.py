# List of Tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Using map and zip
list1, list2 = map(list, zip(*list_of_tuples))

# Output
print("List 1:", list1)
print("List 2:", list2)
