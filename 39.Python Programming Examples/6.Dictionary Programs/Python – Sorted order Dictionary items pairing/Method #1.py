# Python3 code to demonstrate working of
# Sorted order Dictionary items pairing
# Using zip() + sort() + keys() + values()

# initializing dictionary
test_dict = {45 : 3, 7 : 8, 98 : 4, 10 : 12, 65 : 90, 15 : 19}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Sorted order Dictionary items pairing
# Using zip() + sort() + keys() + values()
vals = list(test_dict.values())
vals.sort()
keys = list(test_dict.keys())
keys.sort()
res = dict(zip(keys, vals))

# printing result
print("The sorted order pairing : " + str(res))
