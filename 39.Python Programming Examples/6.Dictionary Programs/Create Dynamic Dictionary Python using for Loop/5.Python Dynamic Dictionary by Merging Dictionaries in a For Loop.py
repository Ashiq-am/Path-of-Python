# Approach 5: Merging Dictionaries in a For Loop
keys = ['name', 'age', 'city']
values = ['Rahul', 25, 'New York']

dynamic_dict = {}
for key, value in zip(keys, values):
	dynamic_dict.update({key: value})

print(dynamic_dict)
