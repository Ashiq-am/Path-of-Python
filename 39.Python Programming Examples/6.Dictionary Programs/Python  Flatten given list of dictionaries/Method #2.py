# Python code to demonstrate
# to flatten list of dictionaries

# Initialising dictionary
ini_dict = [{'a': 1}, {'b': 2}, {'c': 3}]

# printing initial dictionary
print("initial dictionary", str(ini_dict))

# code to flatten lit of dictionary
res = {k: v for d in ini_dict for k, v in d.items()}

# printing result
print("result", str(res))
