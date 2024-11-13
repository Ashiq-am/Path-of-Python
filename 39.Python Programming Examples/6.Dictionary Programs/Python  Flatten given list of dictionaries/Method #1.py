# Python code to demonstrate
# to flatten list of dictionaries

# Initialising dictionary
ini_dict = [{'a': 1}, {'b': 2}, {'c': 3}]

# printing initial dictionary
print("initial dictionary", str(ini_dict))

# code to flatten lit of dictionary
res = {}
for d in ini_dict:
    res.update(d)

# printing result
print("result", str(res))
