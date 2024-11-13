# Python3 code to demonstrate working of
# Filter index similar values
# Using loop + zip() + defaultdict()
from collections import defaultdict

# initializing dictionary
test_dict = {"Gfg": [1, 4, 5, 6, 7], "is": [5, 6, 8, 9, 10],
             "best": [10, 7, 4, 11, 23]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing value list
filt_list = [4, 5, 7]

# Filter index similar values
# Using loop + zip() + defaultdict()
res = defaultdict(list)

for x, y, z in zip(test_dict['Gfg'], test_dict['is'], test_dict['best']):
    if x in filt_list:
        res['Gfg'].append(x)
        res['is'].append(y)
        res['best'].append(z)

# printing result
print("The filtered dictionary : " + str(dict(res)))
