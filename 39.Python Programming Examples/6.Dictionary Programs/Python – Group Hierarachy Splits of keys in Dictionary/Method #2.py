# Python3 code to demonstrate working of
# Group Hierarachy Splits of keys in Dictionary
# Using defaultdict()
from collections import defaultdict

# initializing dictionary
test_dict = {"1-3": 2, "8-7": 0, "1-8": 10, "8-6": 15}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing split char
splt_chr = "-"

res = defaultdict(dict)
for key, val in test_dict.items():
    ini_key, low_key = key.split(splt_chr)

    # defaultdict eliminates check step
    res[ini_key][low_key] = val

# printing result
print("The splitted dictionary : " + str(dict(res)))
