from itertools import groupby

# Sample list of tuples
list_of_tuples = [(1, 2), (3, 4), (1, 2), (5, 6)]

# Sort the list to group similar tuples together
sorted_list = sorted(list_of_tuples)

# Use groupby to eliminate duplicates and generate a set of tuples
set_of_tuples = {next(group) for _, group in groupby(sorted_list)}

# Display the result
print(set_of_tuples)
