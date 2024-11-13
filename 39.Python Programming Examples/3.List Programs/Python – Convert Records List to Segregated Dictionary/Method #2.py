# Python3 code to demonstrate working of
# Convert Records List to Segregated Dictionary
# Using zip() + chain() + cycle() + list comprehension
from itertools import chain, cycle

# initializing list
test_list = [(1, 2), (3, 4), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# initializing index value
frst_idx = "Gfg"
scnd_idx = 'best'

# Convert Records List to Segregated Dictionary
# Using zip() + chain() + cycle() + list comprehension
res = dict(zip(chain(*test_list), cycle([frst_idx, scnd_idx])))

# printing result
print("The constructed Dictionary list : " + str(res))
