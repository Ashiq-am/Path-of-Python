# Initialize list of tuples
list_of_tuples = [(1, 'apple'), (2, 'banana'), (3, 'orange'), (4, 'grape')]

# Extract items with index 1 to 2
sliced_list = [item for index, item in enumerate(list_of_tuples) if 1 <= index < 3]
# Display list of tuples
print(sliced_list)
