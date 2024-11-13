# Python3 code to demonstrate working of
# Duplicate sets in list of sets
# Using Counter() + count() + frozenset() + loop
from collections import Counter

# initializing list
test_list = [{4, 5, 6, 1}, {6, 4, 1, 5}, {1, 3, 4, 3},
             {1, 4, 3}, {7, 8, 9}]

# printing original list
print("The original list is : " + str(test_list))

# getting frequency using Counter()
freqs = Counter(frozenset(sub) for sub in test_list)

res = []
for key, val in freqs.items():

    # if frequency greater than 1, set is appended
    # [duplicate]
    if val > 1:
        res.append(key)

# printing result
print("Duplicate sets list : " + str(res))
