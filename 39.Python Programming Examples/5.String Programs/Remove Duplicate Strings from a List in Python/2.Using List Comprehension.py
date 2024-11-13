# Sample list with duplicate strings
original_list = ['apple', 'orange', 'banana', 'apple', 'grape', 'banana']

# Remove duplicates using list comprehension
unique_list = []
[unique_list.append(item) for item in original_list if item not in unique_list]

print(unique_list)
