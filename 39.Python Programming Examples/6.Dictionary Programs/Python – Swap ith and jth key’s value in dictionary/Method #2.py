# Python3 code to demonstrate working of
# Swap ith and jth key's value in dictionary
# Using values() + dictionary comprehension

# initializing dictionary
test_dict = {"Gfg": 2, "is": 4, "best": 7,
             "for": 9, "geeks": 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing i, j
i, j = 1, 3

# Extracting keys
vals = list(test_dict.values())

# performing swap
vals[i], vals[j] = vals[j], vals[i]

# setting new values
res = {key: vals[idx] for idx, key in enumerate(test_dict)}

# printing result
print("Required dictionary : " + str(res))
