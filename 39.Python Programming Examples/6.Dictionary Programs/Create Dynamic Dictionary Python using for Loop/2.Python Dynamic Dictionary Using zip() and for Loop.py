# Approach 2: Using Zip and For Loop
keys = ['name', 'age', 'city']
values = ['Rahul', 25, 'New York']

dynamic_dict = {}
for key, value in zip(keys, values):
	dynamic_dict[key] = value

print(dynamic_dict)
