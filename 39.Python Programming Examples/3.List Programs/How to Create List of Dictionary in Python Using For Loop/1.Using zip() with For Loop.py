keys = ['key', 'value']

list_of_dicts = [dict(zip(keys, [i, i * 2])) for i in range(3)]

print(list_of_dicts)
