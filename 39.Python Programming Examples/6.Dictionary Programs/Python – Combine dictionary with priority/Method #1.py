# Python3 code to demonstrate working of
# Combine dictionary with priority
# Using loop + copy()

# initializing dictionaries
test_dict1 = {'Gfg': 1, 'is': 2, 'best': 3}
test_dict2 = {'Gfg': 4, 'is': 10, 'for': 7, 'geeks': 12}

# printing original dictionaries
print("The original dictionary is 1 : " + str(test_dict1))
print("The original dictionary is 2 : " + str(test_dict2))

# declaring priority order
prio_dict = {1: test_dict2, 2: test_dict1}

# Combine dictionary with priority
# Using loop + copy()
res = prio_dict[2].copy()
for key, val in prio_dict[1].items():
    res[key] = val

# printing result
print("The dictionary after combination : " + str(res))
