# Define a tuple of lists
tuple_of_lists = ([2, 1, 5], [1, 5, 7], [5, 6, 5])

# Sort each inner list using a lambda function and create a new tuple
sorted_tuple = tuple([*map(int, sorted(sublist))]
					for sublist in tuple_of_lists)

print(sorted_tuple)
