# Python code to find difference in keys in two dictionary

# Initialising dictionary
dict1 = {'key1': 'Geeks', 'key12': 'For'}
dict2 = {'key1': 'Geeks', 'key2': 'For', 'key3': 'geeks',
         'key4': {'GeekKey1': 12, 'GeekKey2': 22, 'GeekKey3': 32}}

for key in dict1.keys():
    if not key in dict2:
        # Printing difference in
        # keys in two dictionary
        print(key)
