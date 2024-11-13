# Sample list of tuples
list_of_tuples = [(1, 2), (3, 4), (1, 2), (5, 6)]

# Create a dictionary to remove duplicates
unique_dict = dict.fromkeys(list_of_tuples)

# Generate a set of tuples using list comprehension
set_of_tuples = set(unique_dict.keys())

# Display the result
print(set_of_tuples)
