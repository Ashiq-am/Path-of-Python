# Python code to demonstrate
# conersion of flattened dictionary
# into nested dictionary

from collections import defaultdict
from functools import reduce
from operator import getitem


def getFromDict(dataDict, mapList):
    # Iterate nested dictionary
    return reduce(getitem, mapList, dataDict)


# instantiate nested defaultdict of defaultdicts
tree = lambda: defaultdict(tree)
d = tree()


# conerting default_dict_to regular dict
def default_to_regular(d):
    """Convert nested defaultdict to regular dict of dicts."""
    if isinstance(d, defaultdict):
        d = {k: default_to_regular(v) for k, v in d.items()}
    return d


# initialising_dictionary
ini_dict = {'Geeks_for_for': 1, 'Geeks_for_geeks': 4,
            'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7}

# priniting initial dictionary
print("initial_dictionary", str(ini_dict))

# code to convert ini_dict to nested dictionary
# iterating_over_dict
for k, v in ini_dict.items():
    # splitting keys
    *keys, final_key = k.split('_')
    getFromDict(d, keys)[final_key] = v

# printing final dictionary
print("final_dictionary", str(default_to_regular(d)))
