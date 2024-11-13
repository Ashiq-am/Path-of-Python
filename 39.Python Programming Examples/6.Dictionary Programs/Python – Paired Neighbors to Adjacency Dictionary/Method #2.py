# Python3 code to demonstrate working of
# Paired Neighbours to Adjacency Dictionary
# Using defaultdict() + loop
from collections import defaultdict

# initializing list
test_list = [(1, 2), (4, 5), (1, 3), (3, 4), (5, 6), (6, 2)]

# printing original list
print("The original list is : " + str(test_list))

# Paired Neighbours to Adjacency Dictionary
# Using defaultdict() + loop
res = defaultdict(set)
for sub in test_list:
    res[sub[0]].add(sub[1])
    res[sub[1]].add(sub[0])

# printing result
print("The Neighbours Paired Dictionary : " + str(dict(res)))
