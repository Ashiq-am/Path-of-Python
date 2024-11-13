# Python3 code to demonstrate working of
# Divide String into Equal K chunks
# Using list comprehension
from collections import Counter

# initializing strings
test_str = 'geeksforgeeks is best for geeks and best for CS'

# printing original string
print("The original string is : " + str(test_str))

# initializing count_list
count_list = ['best', 'geeksforgeeks', 'computer', 'better', 'for', 'and']

# computing frequency using Counter()
res = Counter(test_str.split())

# assigning to list words
res = [res[sub] for sub in count_list]

# printing result
print("The list words frequency : " + str(res))
