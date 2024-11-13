# Python3 code to demonstrate working of
# Unlist Single Valued Dictionary List
# Using loop + isinstance()

# initializing list
test_list = [{'Gfg': 1,
              'is': [{'a': 2, 'b': 3}]},
             {'best': [{'c': 4, 'd': 5}],
              'CS': 6}]

# printing original list
print("The original list is : " + str(test_list))

# Using loop + isinstance()
for dicts in test_list:
    for key, val in dicts.items():

        # isinstance() is used to check for list to convert
        if isinstance(val, list):
            dicts[key] = val[0]

# printing result
print("The converted Dictionary list : " + str(test_list))
