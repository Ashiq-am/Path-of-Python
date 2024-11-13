# Python3 code to demonstrate working of
# Flatten Nested Dictionary to Matrix
# using union() + list comprehension

# initializing dictionary
test_dict = {'Gfg1': {'CS': 1, 'GATE': 2},
             'Gfg2': {'CS': 2, 'GATE': 3},
             'Gfg3': {'CS': 4, 'GATE': 5}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Flatten Nested Dictionary to Matrix
# using union() + list comprehension
temp = set().union(*test_dict.values())
res = [list(test_dict.keys())]
res += [[key] + [sub.get(key, 0) for sub in test_dict.values()] for key in temp]

# printing result
print("The Grouped dictionary list is : " + str(res))
