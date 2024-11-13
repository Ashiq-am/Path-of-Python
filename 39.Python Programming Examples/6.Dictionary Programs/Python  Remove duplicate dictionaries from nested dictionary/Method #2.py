# Python code to demonstrate
# for removing duplicate values from dictionary

# initialising dictionary
ini_dict = {'a': {'b': 1, 'c': 2}, 'b': {'b': 1, 'c': 2},
            'c': {'a': 2, 'b': 3}, 'd': {'a': 2, 'b': 7}}

# printing initial_dictionary
print("initial dictionary", str(ini_dict))

# code to remove duplicates
keep = set({repr(sorted(value.items())): key
            for key, value in ini_dict.items()}.values())

for key in list(ini_dict):
    if key not in keep:
        del ini_dict[key]

# printing result
print("result", str(ini_dict))
