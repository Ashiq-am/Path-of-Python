# Python code to find difference in keys in two dictionary

# Initialising dictionary
dict1 = {'key1': 'Geeks', 'key2': 'For'}
dict2 = {'key1': 'Geeks', 'key2': 'For', 'key3': 'geeks',
         'key4': {'GeekKey1': 12, 'GeekKey2': 22, 'GeekKey3': 32}}

print(set(dict1.keys()).intersection(dict2.keys()))
