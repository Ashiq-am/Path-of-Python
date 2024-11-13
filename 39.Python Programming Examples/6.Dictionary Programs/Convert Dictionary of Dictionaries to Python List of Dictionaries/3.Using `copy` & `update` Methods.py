# Using `copy` and `update` Methods
list_of_dicts = []
for key, value in data.items():
    temp_dict = value.copy()
    temp_dict.update({'id': key})
    list_of_dicts.append(temp_dict)

print(type(data))
print("Result:", list_of_dicts)
print(type(list_of_dicts))
