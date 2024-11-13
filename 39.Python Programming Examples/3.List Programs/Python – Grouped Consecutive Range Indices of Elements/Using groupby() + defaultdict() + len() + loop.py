# Python3 code to demonstrate working of
# Grouped Consecutive Range Indices of Elements
# Using groupby() + defaultdict() + len() + loop
from itertools import groupby
from collections import defaultdict

# initializing lists
test_list = [1, 1, 5, 6, 5, 5, 6, 6, 6, 1, 5, 5]

# printing string
print("The original list : " + str(test_list))

idx = 0
res = defaultdict(list)

# grouping Consecutives
for key, sub in groupby(test_list):
    ele = len(list(sub))

    # append strt index, and till index
    res[key].append((idx, idx + ele - 1))
    idx += ele

# printing results
print("The grouped dictionary : " + str(dict(res)))
