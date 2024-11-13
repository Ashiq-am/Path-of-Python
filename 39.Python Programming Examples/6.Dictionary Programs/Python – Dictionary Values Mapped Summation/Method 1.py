# Python3 code to demonstrate working of
# Dictionary Values Mapped Summation
# Using loop + items()

# initializing dictionary
test_dict = {4: ['a', 'v', 'b', 'e'],
             1: ['g', 'f', 'g'],
             3: ['e', 'v']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# values mapped
map_vals = {'a': 3, 'g': 8, 'f': 10,
            'b': 4, 'e': 7, 'v': 2}

res = dict()
# items() getting keys and values
for key, vals in test_dict.items():
    sum = 0
    for val in vals:
        # summing with mappings
        sum += map_vals[val]
    res[key] = sum

# printing result
print("The extracted values sum : " + str(res))
