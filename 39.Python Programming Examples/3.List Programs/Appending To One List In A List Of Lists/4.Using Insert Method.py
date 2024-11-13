# Create a list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Choose the index of the sublist to append to
index_to_append_to = 1

# Use the insert method to append a single element
list_of_lists[index_to_append_to].insert(len(list_of_lists[index_to_append_to]), 10)

print(list_of_lists)
