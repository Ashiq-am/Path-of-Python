# Approach 3: Dictionary Comprehension with Enumerate
keys = ['name', 'age', 'city']
values = ['Rahul', 25, 'New York']

dynamic_dict = {key: values[i] for i, key in enumerate(keys)}

print(dynamic_dict)
