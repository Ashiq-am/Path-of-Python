# Python3 code to demonstrate working of
# Nested record values summation
# Using loop

# initializing dictionary
test_dict = {'gfg': {'a': 4, 'b': 5, 'c': 6},
             'is': {'a': 2, 'b': 9, 'c': 10},
             'best': {'a': 10, 'b': 2, 'c': 12}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Nested record values summation
# Using loop
res = dict()
for sub in test_dict:
    sum = 0
    for keys in test_dict[sub]:
        sum = sum + test_dict[sub][keys]
    res[sub] = sum

# printing result
print("The dictionary after keys summation is : " + str(res))
