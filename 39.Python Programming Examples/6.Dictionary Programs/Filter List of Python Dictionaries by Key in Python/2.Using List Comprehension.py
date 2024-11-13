# List of dictionaries
list_of_dicts = [{'name': 'A', 'class': 5}, {'name': 'B'}, {'class': 10}]

# Specify the key for filtering
target_key = 'name'

# Filter using list comprehension
filtered_list = [d for d in list_of_dicts if target_key in d]

# Print the result
print("Filtered List :", filtered_list)
