# Python3 code to demonstrate
# Tuple Column element frequency
# using Counter() + list comprehension
from collections import Counter

# initializing list of tuples
test_list = [(1, 'Geeks'), (2, 'for'), (3, 'Geeks')]

# printing the original list
print ("The original list is : " + str(test_list))

# initializing K
K = 1

# using Counter() + list comprehension
# Tuple Column element frequency
res = Counter(i[K] for i in test_list)

# printing result
print ("The frequency of element at Kth index is : " + str(res['Geeks']))
