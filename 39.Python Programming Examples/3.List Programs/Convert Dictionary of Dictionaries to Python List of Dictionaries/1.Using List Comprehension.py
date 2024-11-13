list_of_dicts = [{key: value for key, value in nested_dict.items()} for nested_dict in data.values()]
print(type(data))
print("Result:", list_of_dicts)
print(type(list_of_dicts))
