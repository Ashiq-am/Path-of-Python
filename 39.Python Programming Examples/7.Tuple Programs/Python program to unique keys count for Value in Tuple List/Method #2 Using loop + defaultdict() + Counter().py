# Python3 code to demonstrate working of
# loop + defaultdict() + Counter()
# Using loop + defaultdict() + Counter()
from collections import defaultdict, Counter

# initializing list
test_list = [(3, 4), (1, 2), (2, 4), (8, 2), (7, 2),
             (8, 1), (9, 1), (8, 4), (10, 4)]

# printing original list
print("The original list is : " + str(test_list))

mem_dict = defaultdict(list)
res = []
for sub in test_list:

    # if not in dict, add value
    if sub[0] not in mem_dict[sub[1]]:
        mem_dict[sub[1]].append(sub[0])
        res.append(sub[1])

    # getting frequency
res = dict(Counter(res))

# printing result
print("Unique keys for values : " + str(res))
