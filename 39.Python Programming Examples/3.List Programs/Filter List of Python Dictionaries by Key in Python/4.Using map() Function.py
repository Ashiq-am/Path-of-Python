# List of dictionaries
list_of_dicts = [{'subject': 'Art', 'marks': 25}, {'subject': 'biology'}, {'marks': 30}]

# Specify the key for filtering (ensure case sensitivity)
target_key = 'subject'

# Filter using map and lambda
filtered_list = list(map(lambda d: d if target_key in d else None, list_of_dicts))
filtered_list = [d for d in filtered_list if d is not None]

# Print the result
print("Filtered List:", filtered_list)
