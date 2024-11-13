# Python3 code to demonstrate working of
# Split heterogenous type list
# using defaultdict() + loop
from collections import defaultdict

# initialize list
test_list = ['gfg', 1, 2, 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# Split heterogenous type list
# using defaultdict() + loop
res = defaultdict(list)
for ele in test_list:
    res[type(ele)].append(ele)

# printing result
print("Integer list : " + str(res[int]))
print("String list : " + str(res[str]))
