# Python3 code to demonstrate working of
# Dictionary Values Mapped Summation
# Using dictionary comprehension + sum()

# initializing dictionary
test_dict = {4: ['a', 'v', 'b', 'e'],
             1: ['g', 'f', 'g'],
             3: ['e', 'v']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# values mapped
map_vals = {'a': 3, 'g': 8, 'f': 10,
            'b': 4, 'e': 7, 'v': 2}

# sum() gets sum of each mapped values
res = {key: sum(map_vals[val] for val in vals)
       for key, vals in test_dict.items()}

# printing result
print("The extracted values sum : " + str(res))
