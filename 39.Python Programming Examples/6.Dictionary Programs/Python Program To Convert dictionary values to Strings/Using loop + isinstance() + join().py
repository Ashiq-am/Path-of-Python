# Python3 code to demonstrate working of
# Convert dictionary values to Strings
# Using loop + isinstance()

# initializing dictionary
test_dict = {'Gfg': 4,
             'is': "1",
             'best': [8, 10],
             'geek': (10, 11, 2)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing delims
list_delim, tuple_delim = '-', '^'

res = dict()
for sub in test_dict:

    # checking data types
    if isinstance(test_dict[sub], list):
        res[sub] = list_delim.join([str(ele) for ele in test_dict[sub]])
    elif isinstance(test_dict[sub], tuple):
        res[sub] = tuple_delim.join(list([str(ele) for ele in test_dict[sub]]))
    else:
        res[sub] = str(test_dict[sub])

# printing result
print("The converted dictionary : " + str(res))
