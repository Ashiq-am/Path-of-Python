# Python code to demonstrate
# conversion of nested dictionary
# into flattened dictionary

from collections import MutableMapping


# code to convert ini_dict to flattened dictionary
# default seperater '_'
def convert_flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k

        if isinstance(v, MutableMapping):
            items.extend(convert_flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


# initialising_dictionary
ini_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}

# priniting initial dictionary
print("initial_dictionary", str(ini_dict))

# printing final dictionary
print("final_dictionary", str(convert_flatten(ini_dict)))
