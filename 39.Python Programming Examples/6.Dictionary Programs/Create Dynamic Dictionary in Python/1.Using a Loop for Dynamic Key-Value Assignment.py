# initialize lists for keys and values
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# initialize empty dictionary
dynamic_dict = {}

# dynamically assign key-value pairs using a loop
for i in range(len(keys)):
	dynamic_dict[keys[i]] = values[i]

# print the resulting dictionary
print(dynamic_dict)
