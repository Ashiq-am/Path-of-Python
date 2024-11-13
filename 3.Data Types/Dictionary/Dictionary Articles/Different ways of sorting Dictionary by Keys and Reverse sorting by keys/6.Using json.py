# Importing json
import json

# Initialising a dictionary
my_dict = {"b": 2, "c": 3, "a": 1,"d":4}

# Sorting and printind in a single line
print("Sorted dictionary is : ", json.dumps(my_dict, sort_keys=True))
