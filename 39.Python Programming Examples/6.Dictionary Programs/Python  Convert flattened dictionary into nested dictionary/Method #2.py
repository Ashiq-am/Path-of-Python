# Python code to demonstrate
# conersion of flattened dictionary
# into nested dictionary

# code to conert dict into nested dict
def nest_dict(dict1):
    result = {}
    for k, v in dict1.items():
        # for each key call method split_rec which
        # will split keys to form recursively
        # nested dictionary
        split_rec(k, v, result)
    return result


def split_rec(k, v, out):
    # splitting keys in dict
    # calling_recursively to break items on '_'
    k, *rest = k.split('_', 1)
    if rest:
        split_rec(rest[0], v, out.setdefault(k, {}))
    else:
        out[k] = v


# initialising_dictionary
ini_dict = {'Geeks_for_for': 1, 'Geeks_for_geeks': 4,
            'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7}

# priniting initial dictionary
print("initial_dictionary", str(ini_dict))

# printing final dictionary
print("final_dictionary", str(nest_dict(ini_dict)))
