# Input set of tuples
tuple_set = {(1, 2), (3, 4), (5, 6)}

# Convert set of tuples to list of lists using map() function
list_of_lists = list(map(list, tuple_set))

# Output
print(list_of_lists)
