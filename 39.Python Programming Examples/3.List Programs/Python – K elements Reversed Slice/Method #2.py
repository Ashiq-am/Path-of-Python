# Python3 code to demonstrate working of
# K elements Reversed Slice
# Using K elements Reversed Slice
from itertools import islice

# initializing list
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 6

# using revered and islice to slice
# and then perform reverse
res = list(islice(reversed(test_list), K))

# printing result
print("The sliced list : " + str(res))
