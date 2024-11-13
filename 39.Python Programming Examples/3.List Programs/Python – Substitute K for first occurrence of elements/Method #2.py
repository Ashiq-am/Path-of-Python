# Python3 code to demonstrate working of
# Substitute K for first occurrence of elements
# Using defaultdict() + next() + count + list comprehension
from itertools import count
from collections import defaultdict

# initializing list
test_list = [4, 3, 3, 7, 8, 7, 4, 6, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 10

# Substitute K for first occurrence of elements
# Using defaultdict() + next() + count + list comprehension
freq = defaultdict(count)
temp = [int(next(freq[val]) == 0) for val in test_list]
res = [K if ele else test_list[idx] for idx, ele in enumerate(temp)]

# printing result
print("List after Substitution : " + str(res))
