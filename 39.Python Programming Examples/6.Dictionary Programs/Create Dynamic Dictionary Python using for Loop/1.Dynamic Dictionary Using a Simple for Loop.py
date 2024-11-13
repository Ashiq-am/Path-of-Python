# Approach 1: Using a Simple For Loop
keys = ['name', 'age', 'city']
values = ['Rahul', 25, 'New York']

dynamic_dict = {}
for i in range(len(keys)):
	dynamic_dict[keys[i]] = values[i]

print(dynamic_dict)
