# Python3 code to demonstrate working of
# Convert list elements to bi-tuples
# using zip() + repeat()
from itertools import repeat

# initialize list
test_list = [5, 6, 7, 8, 4, 3]

# printing original list
print("The original list is : " + str(test_list))

# initialize attach element
ele = 'gfg'

# Convert list elements to bi-tuples
# using zip() + repeat()
res = list(zip(test_list, repeat(ele)))

# printing result
print("Tuple list after attaching element : " + str(res))
