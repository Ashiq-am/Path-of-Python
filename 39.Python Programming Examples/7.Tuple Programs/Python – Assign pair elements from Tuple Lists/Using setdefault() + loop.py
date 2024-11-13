# Python3 code to demonstrate working of
# Assign pair elements from Tuple Lists
# Using setdefault + loop

# initializing list
test_list = [(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)]

# printing string
print("The original list : " + str(test_list))

# initializing dictionary
res = dict()
for key, val in test_list:
    # adding to both, corresponding keys and values
    res.setdefault(val, [])
    res.setdefault(key, []).append(val)

# printing results
print("The resultant pairings : " + str(res))
