# Python3 code to demonstrate working of
# Cumulative Keys Mean in Dictionary List
# Using defaultdict() + mean()
from statistics import mean
from collections import defaultdict

# initializing list
test_list = [{'gfg': 34, 'is': 8, 'best': 10},
             {'gfg': 1, 'for': 10, 'geeks': 9, 'and': 5, 'best': 12},
             {'geeks': 8, 'find': 3, 'gfg': 3, 'best': 8}]

# printing original list
print("The original list is : " + str(test_list))

# defaultdict reduces step to memoize.
res = defaultdict(list)
for sub in test_list:
    for key, val in sub.items():
        res[key].append(val)

res = dict(res)
for key, num_l in res.items():
    # computing mean
    res[key] = mean(num_l)

# printing result
print("The Extracted average : " + str(res))
