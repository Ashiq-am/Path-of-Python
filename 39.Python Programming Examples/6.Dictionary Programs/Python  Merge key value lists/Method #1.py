# Python3 code to demonstrate working of
# Merge key value list
# Using zip() + loop + defaultdict()
from collections import defaultdict

# initializing lists
test_list1 = [0, 0, 0, 1, 1, 1, 2, 2]
test_list2 = ['gfg', 'is', 'best', 'Akash', 'Akshat', 'Nikhil', 'apple', 'grapes']

# printing original lists
print("The original list1 is : " + str(test_list1))
print("The original list2 is : " + str(test_list2))

# Using zip() + loop + defaultdict()
# Merge key value list
res = defaultdict(list)
for i, j in zip(test_list1, test_list2):
    res[i].append(j)

# printing result
print("The merged key value dictionary is : " + str(dict(res)))
