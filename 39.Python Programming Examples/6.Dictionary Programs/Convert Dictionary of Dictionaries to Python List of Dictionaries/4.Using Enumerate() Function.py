# Using Enumerate
list_of_dicts = [{**value, 'id': key} for key, value in enumerate(data.values(), 1)]

print(type(data))
print("Result:", list_of_dicts)
print(type(list_of_dicts))
