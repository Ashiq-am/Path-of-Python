# Python3 code to demonstrate working of
# Mutiple Keys Grouped Summation
# Using loop + defaultdict() + list comprehension
from collections import defaultdict

# initializing list
test_list = [(12, 'M', 'Gfg'), (23, 'H', 'Gfg'),
             (13, 'M', 'Best'), (18, 'M', 'Gfg'),
             (2, 'H', 'Gfg'), (23, 'M', 'Best')]

# printing original list
print("The original list is : " + str(test_list))

# initializing grouping indices
grp_indx = [1, 2]

# initializing sum index
sum_idx = [0]

# Mutiple Keys Grouped Summation
# Using loop + defaultdict() + list comprehension
temp = defaultdict(int)
for sub in test_list:
    temp[(sub[grp_indx[0]], sub[grp_indx[1]])] += sub[sum_idx[0]]
res = [key + (val,) for key, val in temp.items()]

# printing result
print("The grouped summation : " + str(res))
