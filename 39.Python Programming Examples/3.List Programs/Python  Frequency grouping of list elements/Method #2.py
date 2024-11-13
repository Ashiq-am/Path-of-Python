# Python3 code to demonstrate working of
# Frequency grouping of list elements
# using Counter() + items()
from collections import Counter

# initialize list
test_list = [1, 3, 3, 1, 4, 4]

# printing original list
print("The original list : " + str(test_list))

# Frequency grouping of list elements
# using Counter() + items()
res = list(Counter(test_list).items())

# printing result
print("Frequency of list elements : " + str(res))
