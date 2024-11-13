# Python3 code to demonstrate working of
# Remove all Duplicate occurring records
# Using list comprehension + Counter() + items()
from collections import Counter

# initialize list
test_list = [(3, 4), (4, 5), (3, 6), (3, 4), (4, 5), (6, 7)]

# printing original list
print("The original list : " + str(test_list))

# Remove all Duplicate occurring records
# Using list comprehension + Counter() + items()
res = [ele for ele, count in Counter(test_list).items() if count == 1]

# printing result
print("All the non Duplicate from list are : " + str(res))
