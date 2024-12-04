dict1 = {'name': 'Alice'}
dict2 = {'age': 25}
dict1.update(dict2)  # Merges dict2 into dict1
print(dict1)

# Using unpacking
merged_dict = {**dict1, **dict2}
print(merged_dict)