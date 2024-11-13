# List of dictionaries
list_of_dicts = [{'name': 'Alice', 'age': 25}, {'name': 'Bob'}, {'age': 30}]

# Specify the key for filtering
target_key = 'name'

# Filter using filter and lambda
filtered_list = list(filter(lambda d: target_key in d, list_of_dicts))

# Print the result
print("Filtered List :", filtered_list)
