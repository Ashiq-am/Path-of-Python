# initializing dictionary
test_dict = {'Gfg': 4, 'is': 1, 'best': 8, 'for': 10, 'geeks': 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing swap indices
i, j = 1, 3

# conversion to tuples
tups = list(test_dict.items())

# swapping by indices
tups[i], tups[j] = tups[j], tups[i]

# converting back
res = dict(tups)

# printing result
print("The swapped dictionary : " + str(res))
