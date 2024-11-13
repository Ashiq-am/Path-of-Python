# Python3 code to demonstrate working of
# Unique keys count for Value in Tuple List
# Using loop + defaultdict()
from collections import defaultdict

# initializing list
test_list = [(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9, 1), (8, 4), (10, 4)]

# printing original list
print("The original list is : " + str(test_list))

res = defaultdict(list)
for sub in test_list:
    # getting all keys to values
    res[sub[1]].append(sub[0])

res = dict(res)

res_dict = dict()
for key in res:
    # getting unique key counts for each value
    res_dict[key] = len(list(set(res[key])))

# printing result
print("Unique keys for values : " + str(res_dict))
