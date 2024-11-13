# Python3 code to demonstrate working of
# Group similar elements into Matrix
# Using list comprehension + Counter()
from collections import Counter

# initializing list
test_list = [1, 3, 5, 1, 3, 2, 5, 4, 2]

# printing original list
print("The original list : " + str(test_list))

# Group similar elements into Matrix
# Using list comprehension + Counter()
temp = Counter(test_list)
res = [[key] * val for key, val in temp.items()]

# printing result
print("Matrix after grouping : " + str(res))
