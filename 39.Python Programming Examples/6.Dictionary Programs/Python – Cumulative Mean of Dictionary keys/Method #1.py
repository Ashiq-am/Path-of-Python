# Python3 code to demonstrate working of
# Cumulative Keys Mean in Dictionary List
# Using loop + mean()
from statistics import mean

# initializing list
test_list = [{'gfg': 34, 'is': 8, 'best': 10},
             {'gfg': 1, 'for': 10, 'geeks': 9, 'and': 5, 'best': 12},
             {'geeks': 8, 'find': 3, 'gfg': 3, 'best': 8}]

# printing original list
print("The original list is : " + str(test_list))

res = dict()
for sub in test_list:
    for key, val in sub.items():
        if key in res:

            # combining each key to all values in
            # all dictionaries
            res[key].append(val)
        else:
            res[key] = [val]

for key, num_l in res.items():
    res[key] = mean(num_l)

# printing result
print("The Extracted average : " + str(res))
