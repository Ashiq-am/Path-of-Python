# List of Tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Iterative Unpacking
list1, list2 = [], []
for item in list_of_tuples:
	val1, val2 = item
	list1.append(val1)
	list2.append(val2)

# Output
print("List 1:", list1)
print("List 2:", list2)
