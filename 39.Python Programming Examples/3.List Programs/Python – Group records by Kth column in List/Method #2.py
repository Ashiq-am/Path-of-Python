# Python3 code to demonstrate
# Group records by Kth column in List
# using itemgetter() + list comprehension + groupby()
from operator import itemgetter
from itertools import groupby

# Initializing list
test_list = [('Gfg', 1), ('is', 2), ('Gfg', 3), ('is', 4), ('best', 5)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 0

# Group records by Kth column in List
# using loop + defaultdict()
temp = itemgetter(K)
res = [list(val) for key, val in groupby(sorted(test_list, key = temp), temp)]

# printing result
print ("The list after grouping : " + str(res))
