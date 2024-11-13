# Python3 code to demonstrate working of
# Extract Similar pairs from List
# Using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [4, 6, 7, 4, 2, 6, 2, 8]

# printing original list
print("The original list is : " + str(test_list))

# Extract Similar pairs from List
# Using Counter() + list comprehension
res = [(key, key) for key, val in Counter(test_list).items()
       for _ in range(val // 2)]

# printing result
print("The records after pairing : " + str(res))
