# Python3 code to demonstrate working of
# Group single item dictionaries into List values
# Using defaultdict() + * operator + loop
from collections import defaultdict

# initializing lists
test_list = [{"Gfg": 3}, {"is": 8}, {"Best": 10}, {"Gfg": 18}, {"Best": 33}]

# printing original list
print("The original list : " + str(test_list))

res = defaultdict(list)
for ele in test_list:
    # using * operator to unpack
    # reducing one loop
    key, val = tuple(*ele.items())
    res[key].append(val)

# printing result
print("The constructed dictionary : " + str(dict(res)))
