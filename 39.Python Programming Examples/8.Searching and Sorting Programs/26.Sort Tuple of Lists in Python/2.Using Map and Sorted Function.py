# Define a tuple of lists
tuple_of_lists = ([2, 1, 5], [1, 5, 7], [5, 6, 5])

# Use map to apply the sorted function to each inner list and create a new tuple
sorted_tuple = tuple(map(sorted, tuple_of_lists))

print(sorted_tuple)
